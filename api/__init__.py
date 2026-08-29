"""
Vercel Serverless API for Python Learning Repository
=====================================================

This module provides serverless API endpoints compatible with Vercel.
It demonstrates how to deploy Python applications on Vercel.

Endpoints:
- GET /api/health - Health check endpoint
- GET /api/status - System status
- GET /api/lessons - List of available lessons
- GET /api/run?script=<name> - Run a Python script remotely
"""

import json
import os
import sys
from datetime import datetime, timezone
from typing import Dict, Any, Optional


def get_utc_now() -> str:
    """Get current UTC time in ISO format"""
    return datetime.now(timezone.utc).isoformat()


def health_check(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """
    Health check endpoint for Vercel
    
    Returns:
        JSON response with health status
    """
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'status': 'healthy',
            'timestamp': get_utc_now(),
            'environment': os.environ.get('VERCEL_ENV', 'development'),
            'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        })
    }


def get_status(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """
    Get system status and repository information
    
    Returns:
        JSON response with system status
    """
    # Count available lessons and projects
    base_dir = os.path.dirname(os.path.dirname(__file__))
    
    lesson_count = 0
    project_count = 0
    
    # Count lesson directories
    for item in os.listdir(base_dir):
        if item.startswith(('01-', '02-', '03-', '04-', '05-', '06-', '07-', '08-', '09-', '10-')):
            lesson_count += 1
    
    # Count projects
    projects_dir = os.path.join(base_dir, 'projects')
    if os.path.exists(projects_dir):
        for category in os.listdir(projects_dir):
            category_path = os.path.join(projects_dir, category)
            if os.path.isdir(category_path):
                project_count += len([f for f in os.listdir(category_path) if f.endswith('.py')])
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'repository': 'Python Learning Repository',
            'version': '1.0.0',
            'lessons_available': lesson_count,
            'projects_available': project_count,
            'features': [
                'Interactive Python tutorials',
                'Beginner to Advanced projects',
                'Code exercises with solutions',
                'Best practices and patterns'
            ],
            'timestamp': get_utc_now()
        })
    }


def get_lessons(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """
    Get list of available lessons
    
    Returns:
        JSON response with lessons list
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))
    
    lessons = []
    for item in sorted(os.listdir(base_dir)):
        if item.startswith(('01-', '02-', '03-', '04-', '05-', '06-', '07-', '08-', '09-', '10-')):
            item_path = os.path.join(base_dir, item)
            if os.path.isdir(item_path):
                # Count Python files in the lesson
                py_files = [f for f in os.listdir(item_path) if f.endswith('.py')]
                
                # Extract lesson number and name
                parts = item.split('-', 1)
                lesson_num = parts[0] if len(parts) > 0 else ''
                lesson_name = parts[1].replace('-', ' ').title() if len(parts) > 1 else item
                
                lessons.append({
                    'number': lesson_num,
                    'name': lesson_name,
                    'directory': item,
                    'files_count': len(py_files),
                    'files': py_files
                })
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'total_lessons': len(lessons),
            'lessons': lessons
        })
    }


def run_script(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """
    Run a Python script from the repository (demo purpose)
    
    Query Parameters:
        script: Name of the script to run (e.g., 'hello_world')
    
    Returns:
        JSON response with script output or error
    """
    # Get query parameters
    query_string = event.get('queryStringParameters', {}) or {}
    script_name = query_string.get('script', 'hello_world')
    
    # Security: Only allow specific safe scripts
    allowed_scripts = ['hello_world', 'variables', 'operators', 'calculator']
    
    if script_name not in allowed_scripts:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': f'Script "{script_name}" is not in the allowed list',
                'allowed_scripts': allowed_scripts
            })
        }
    
    try:
        # Find and execute the script
        base_dir = os.path.dirname(os.path.dirname(__file__))
        
        # Search for the script
        script_path = None
        for root, dirs, files in os.walk(base_dir):
            if f'{script_name}.py' in files:
                script_path = os.path.join(root, f'{script_name}.py')
                break
        
        if not script_path:
            return {
                'statusCode': 404,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'error': f'Script "{script_name}.py" not found'
                })
            }
        
        # Execute the script safely
        import io
        from contextlib import redirect_stdout
        
        f = io.StringIO()
        with redirect_stdout(f):
            # Read and execute the script content
            with open(script_path, 'r') as file:
                code = file.read()
                exec(code, {'__name__': '__main__'})
        
        output = f.getvalue()
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'script': script_name,
                'output': output.strip(),
                'success': True
            })
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': str(e),
                'script': script_name
            })
        }


# Vercel serverless function handlers
def handler(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """
    Main handler for Vercel serverless functions
    
    Routes requests to appropriate handlers based on path
    """
    # Get the request path
    path = event.get('path', '/')
    http_method = event.get('httpMethod', 'GET')
    
    # Route mapping
    routes = {
        ('GET', '/api/health'): health_check,
        ('GET', '/api/status'): get_status,
        ('GET', '/api/lessons'): get_lessons,
        ('GET', '/api/run'): run_script,
    }
    
    # Find matching route
    handler_func = routes.get((http_method, path))
    
    if handler_func:
        return handler_func(event, context)
    else:
        return {
            'statusCode': 404,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': 'Endpoint not found',
                'available_endpoints': [
                    'GET /api/health',
                    'GET /api/status',
                    'GET /api/lessons',
                    'GET /api/run?script=<name>'
                ]
            })
        }


# Individual function exports for Vercel
def health(event, context=None):
    """Vercel entry point for /api/health"""
    return health_check(event, context)


def status(event, context=None):
    """Vercel entry point for /api/status"""
    return get_status(event, context)


def lessons(event, context=None):
    """Vercel entry point for /api/lessons"""
    return get_lessons(event, context)


def run(event, context=None):
    """Vercel entry point for /api/run"""
    return run_script(event, context)


# For local testing
if __name__ == '__main__':
    print("Testing Vercel API endpoints locally...")
    print("=" * 60)
    
    # Test health endpoint
    print("\n🏥 Testing /api/health")
    result = health_check({})
    print(f"Status: {result['statusCode']}")
    print(f"Response: {result['body']}")
    
    # Test status endpoint
    print("\n📊 Testing /api/status")
    result = get_status({})
    print(f"Status: {result['statusCode']}")
    print(f"Response: {result['body']}")
    
    # Test lessons endpoint
    print("\n📚 Testing /api/lessons")
    result = get_lessons({})
    print(f"Status: {result['statusCode']}")
    response_data = json.loads(result['body'])
    print(f"Total lessons: {response_data['total_lessons']}")
    for lesson in response_data['lessons'][:3]:  # Show first 3
        print(f"  - {lesson['number']}: {lesson['name']} ({lesson['files_count']} files)")
    
    print("\n" + "=" * 60)
    print("✅ All tests completed!")
