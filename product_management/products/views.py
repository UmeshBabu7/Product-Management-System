from django.shortcuts import render, redirect
import os
import pandas as pd
import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
import json


# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def upload_file(request):
    """API endpoint for file upload and processing"""
    try:
        if 'file' not in request.FILES:
            return Response(
                {'error': 'No file provided'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        file = request.FILES['file']
        
        # Validate file type
        allowed_extensions = ['.csv', '.xlsx', '.xls']
        file_extension = os.path.splitext(file.name)[1].lower()
        
        if file_extension not in allowed_extensions:
            return Response(
                {'error': 'Invalid file type. Please upload CSV or Excel files only.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Save file temporarily
        file_path = default_storage.save(f'temp/{file.name}', ContentFile(file.read()))
        full_path = default_storage.path(file_path)
        
        # Process the file
        result = process_file(full_path, file_extension)
        
        # Clean up temporary file
        default_storage.delete(file_path)
        
        return Response(result, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response(
            {'error': f'Error processing file: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


def process_file(file_path, file_extension):
    """Process uploaded file and import data"""
    try:
        # Read file based on extension
        if file_extension == '.csv':
            df = pd.read_csv(file_path)
        else:  # Excel files
            df = pd.read_excel(file_path)
        
        # Validate required columns
        required_columns = ['sku', 'name', 'category', 'price', 'stock_qty', 'status']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            return {
                'error': f'Missing required columns: {", ".join(missing_columns)}',
                'success': False
            }
        
        # Clean and validate data
        df = df.dropna(subset=['sku', 'name'])  # Remove rows with missing SKU or name
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df['stock_qty'] = pd.to_numeric(df['stock_qty'], errors='coerce')
        
        # Remove rows with invalid numeric data
        df = df.dropna(subset=['price', 'stock_qty'])
        
        # Ensure status values are valid
        valid_statuses = ['active', 'inactive']
        df = df[df['status'].isin(valid_statuses)]
        
        # Import data
        imported_count = 0
        updated_count = 0
        errors = []
        
        for _, row in df.iterrows():
            try:
                product, created = Product.objects.update_or_create(
                    sku=row['sku'],
                    defaults={
                        'name': row['name'],
                        'category': row['category'],
                        'price': row['price'],
                        'stock_qty': int(row['stock_qty']),
                        'status': row['status']
                    }
                )
                
                if created:
                    imported_count += 1
                else:
                    updated_count += 1
                    
            except Exception as e:
                errors.append(f"Error processing SKU {row['sku']}: {str(e)}")
        
        return {
            'success': True,
            'imported': imported_count,
            'updated': updated_count,
            'errors': errors,
            'total_processed': len(df)
        }
        
    except Exception as e:
        return {
            'error': f'Error processing file: {str(e)}',
            'success': False
        }
