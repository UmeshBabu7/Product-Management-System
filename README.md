# Product Management System

A Django-based system for uploading, parsing, and managing product data from Excel/CSV files. This system provides a complete data ingestion and validation workflow with a user-friendly interface and comprehensive admin panel.

## Features

- **File Upload**: Accept CSV and Excel files (.csv, .xlsx, .xls)
- **Data Validation**: Comprehensive validation for required fields and data types
- **Duplicate Handling**: Smart handling of existing products (update vs. create)
- **Django Admin Interface**: Full-featured admin panel with filtering, searching, paginating, ordering
- **REST API**: RESTful API endpoints

## Tech Stack

- **Backend**: Django
- **Database**: SQLite
- **Data Processing**: Pandas, OpenPyXL
- **API**: Django REST Framework
- **Frontend**: HTML, CSS, JavaScript

## Project Structure

```
Product-Management-System/                    # Root project directory
├── README.md                                 # Project documentation
├── requirements.txt                          # Python dependencies
├── venv/                                     # Virtual environment
│   ├── Scripts/                             # Windows activation scripts
│   ├── Lib/                                 # Python packages
│   └── pyvenv.cfg                           # Virtual environment config
└── product_management/                       # Main Django project directory
    ├── manage.py                            # Django management script
    ├── db.sqlite3                           # SQLite database file
    ├── create_sample_data.py                # Script to generate sample data
    ├── sample_products.csv                  # Sample CSV data file
    ├── sample_products.xlsx                 # Sample Excel data file
    ├── media/                               # Media files directory
    │   └── temp/                            # Temporary file storage
    ├── product_management/                  # Django project settings package
    │   ├── __init__.py                      # Package initialization
    │   ├── __pycache__/                     # Python cache files
    │   ├── settings.py                      # Django settings configuration
    │   ├── urls.py                          # Main URL configuration
    │   ├── wsgi.py                          # WSGI application entry point
    │   └── asgi.py                          # ASGI application entry point
    └── products/                            # Products Django app
        ├── __init__.py                      # App initialization
        ├── __pycache__/                     # Python cache files
        ├── admin.py                         # Django admin configuration
        ├── apps.py                          # App configuration
        ├── models.py                        # Product model definitions
        ├── views.py                         # API views and file upload logic
        ├── serializers.py                   # Django REST Framework serializers
        ├── urls.py                          # App URL patterns
        ├── tests.py                         # Unit tests
        ├── migrations/                      # Database migrations
        │   ├── __init__.py                  # Migrations package
        │   ├── __pycache__/                 # Python cache files
        │   └── 0001_initial.py             # Initial migration
        └── templates/                       # HTML templates
            └── products/                    # App-specific templates
                └── upload.html              # File upload page template
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone/Download the Project

```
# If using git
git clone https://github.com/UmeshBabu7/Product-Management-System.git
cd Product_Management-System
cd product_management

git status
git add .
git commit -m ""
git push origin main

# Or download and extract the project files
```

### Step 2: Install Dependencies

```
pip install -r requirements.txt
```

### Step 3: Database Setup

```
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser
```

### Step 4: Run the Development Server

```
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

### Web Interface

1. **Upload Page**: Navigate to `http://127.0.0.1:8000/upload/`
   - Drag and drop or click to select CSV/Excel files
   - Detailed import results

2. **Admin Panel**: Navigate to `http://127.0.0.1:8000/admin/`
   - Username: `admin`
   - Password: `admin@@@1234567`
   - View, edit, and manage all products
   - Advanced filtering and search capabilities

### API Endpoints

#### Upload File
```http
POST /api/upload/
Content-Type: multipart/form-data

Body: file (CSV/Excel file)
```

**Response:**
```json
{
    "success": true,
    "imported": 5,
    "updated": 2,
    "errors": [],
    "total_processed": 7
}
```

#### List Products
```http
GET /api/products/
```

**Response:**
```json
[
     {
        "id": 1,
        "sku": "SKU0001",
        "name": "Product 1",
        "category": "Clothing",
        "price": "232.54",
        "stock_qty": 189,
        "status": "inactive",
        "is_in_stock": true,
        "is_active": false,
        "created_at": "2025-09-15T02:14:15.858235Z",
        "updated_at": "2025-09-15T03:33:43.584509Z"
    },
]
```

#### Get Product by SKU
```http
GET /api/products/{sku}/
```

**Response:**
```json
 {
        "id": 1,
        "sku": "SKU0001",
        "name": "Product 1",
        "category": "Clothing",
        "price": "232.54",
        "stock_qty": 189,
        "status": "inactive",
        "is_in_stock": true,
        "is_active": false,
        "created_at": "2025-09-15T02:14:15.858235Z",
        "updated_at": "2025-09-15T03:33:43.584509Z"
    }
```

## Data Format Requirements

### Required Columns

Your CSV/Excel file must contain the following columns:

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `sku` | String | Unique product identifier | "SKU0001" |
| `name` | String | Product name | "Product 1" |
| `category` | String | Product category | "Clothing" |
| `price` | Decimal | Product price | 232.54 |
| `stock_qty` | Integer | Stock quantity | 189 |
| `status` | String | Product status | "active" or "inactive" |

### Valid Categories

- Clothing
- Electronics
- Home
- Sports
- Books
- Beauty

### Valid Status Values

- `active`
- `inactive`

### Sample Data

Use the provided `sample_products.csv` or `sample_products.xlsx` files as templates.

## Data Processing Logic

### Validation Rules

1. **File Type**: Only CSV (.csv) and Excel (.xlsx, .xls) files are accepted
2. **Required Fields**: All 6 columns must be present
3. **Data Types**: 
   - `price` must be numeric
   - `stock_qty` must be numeric
   - `status` must be 'active' or 'inactive'
4. **SKU Uniqueness**: SKU values must be unique within the file

### Duplicate Handling

- **New Products**: Products with SKUs not in the database are created
- **Existing Products**: Products with existing SKUs are updated with new data
- **Error Handling**: Invalid rows are skipped with detailed error messages

### Data Cleaning

- Empty rows are automatically removed
- Invalid numeric values are filtered out
- Invalid status values are excluded

## Admin Interface Features

### Product Management

- **List View**: Paginated list with sortable columns
- **Filters**: Filter by category, status, and creation date
- **Search**: Search by SKU, name, or category
- **Bulk Edit**: Edit multiple products simultaneously
- **Export**: Export product data to CSV

### Advanced Features

- **Fieldsets**: Organized form layout for better UX
- **Read-only Fields**: Timestamps are automatically managed
- **Validation**: Real-time validation in admin forms

## Configuration

### Database Configuration

The system uses SQLite by default.

1. Update `DATABASES` in `settings.py`
2. Run migrations

### File Upload Settings

- **Max File Size**: Configure in Django settings
- **Allowed Extensions**: Currently supports .csv, .xlsx, .xls
- **Temporary Storage**: Files are processed and immediately deleted

## Error Handling

### Common Issues

1. **Missing Columns**: Ensure all required columns are present
2. **Invalid Data Types**: Check that price and stock_qty are numeric
3. **File Format**: Verify file is CSV or Excel format
4. **Large Files**: Consider chunking very large files

### Error Messages

The system provides detailed error messages for:
- File format validation
- Column validation
- Data type validation
- Individual row processing errors

## Development

### Running Tests

```
python manage.py test
```

### Adding New Features

1. Create new models in `models.py`
2. Add serializers in `serializers.py`
3. Create views in `views.py`
4. Update URLs in `urls.py`
5. Create/update templates as needed

### Code Structure

- **Models**: Database schema and business logic
- **Views**: Request handling and data processing
- **Serializers**: API data transformation
- **Templates**: User interface
- **URLs**: Routing configuration

## Production Deployment

### Security Considerations

1. Change the default admin password
2. Set `DEBUG = False` in production
3. Configure proper database credentials
4. Enable HTTPS

### Performance Optimization

1. Set up media file serving

### Common Issues

1. **Import Errors**: Check that all dependencies are installed
2. **Database Errors**: Ensure migrations are applied
3. **File Upload Issues**: Check file permissions and size limits
4. **Admin Access**: Verify superuser creation

