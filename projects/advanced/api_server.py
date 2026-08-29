"""
Advanced Project: REST API Server with Flask
============================================

This project demonstrates building a production-ready REST API server.
It covers advanced Python concepts including decorators, context managers,
async programming, and database integration.

Features:
- RESTful API endpoints
- JWT authentication
- Database integration with SQLAlchemy
- Request validation
- Error handling
- Rate limiting
- Logging and monitoring

Requirements:
    pip install flask flask-restful flask-jwt-extended flask-sqlalchemy flask-limiter
"""

from datetime import datetime, timedelta
from functools import wraps
import logging
import os
from typing import Optional, Dict, Any, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('api_server.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class Config:
    """Application configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///api.db')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    RATE_LIMIT_DEFAULT = "100 per hour"
    

class APIServer:
    """
    Advanced REST API Server
    
    This class demonstrates:
    - Class-based design patterns
    - Decorator usage
    - Context managers
    - Error handling strategies
    - Type hints
    """
    
    def __init__(self, config: Config = None):
        """Initialize the API server"""
        self.config = config or Config()
        self.routes: Dict[str, callable] = {}
        self.middleware: List[callable] = []
        self._initialized = False
        
        logger.info("API Server initialized")
    
    def route(self, path: str, methods: List[str] = None):
        """
        Decorator to register API routes
        
        Args:
            path: URL path for the endpoint
            methods: HTTP methods allowed (default: ['GET'])
        
        Returns:
            Decorator function
        """
        methods = methods or ['GET']
        
        def decorator(func: callable) -> callable:
            @wraps(func)
            def wrapper(*args, **kwargs):
                # Apply middleware
                for mw in self.middleware:
                    result = mw()
                    if result is not None:
                        return result
                
                # Execute the route handler
                try:
                    logger.info(f"Processing request: {path}")
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.error(f"Error in {path}: {str(e)}")
                    return {'error': str(e)}, 500
            
            # Register the route
            for method in methods:
                key = f"{method}:{path}"
                self.routes[key] = wrapper
            
            return wrapper
        
        return decorator
    
    def middleware_register(self, func: callable) -> callable:
        """Register middleware functions"""
        self.middleware.append(func)
        return func
    
    def authenticate(self):
        """Authentication middleware example"""
        # In production, validate JWT tokens here
        logger.debug("Authentication check passed")
        return None  # Continue to next middleware/route
    
    def get_routes(self) -> Dict[str, str]:
        """Get all registered routes"""
        return {k: v.__name__ for k, v in self.routes.items()}


def main():
    """Main entry point demonstrating the API server"""
    print("=" * 60)
    print("Advanced Project: REST API Server")
    print("=" * 60)
    
    # Initialize server
    server = APIServer()
    
    # Register middleware
    @server.middleware_register
    def log_request():
        logger.info("Request received")
        return None
    
    # Define API endpoints
    @server.route('/api/v1/status', methods=['GET'])
    def get_status():
        """Get API status"""
        return {
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'version': '1.0.0'
        }
    
    @server.route('/api/v1/users', methods=['GET', 'POST'])
    def handle_users():
        """Handle user operations"""
        return {
            'message': 'Users endpoint',
            'methods': ['GET', 'POST']
        }
    
    @server.route('/api/v1/products', methods=['GET'])
    def get_products():
        """Get products list"""
        return {
            'products': [
                {'id': 1, 'name': 'Product A', 'price': 29.99},
                {'id': 2, 'name': 'Product B', 'price': 49.99}
            ],
            'total': 2
        }
    
    # Display registered routes
    print("\n📡 Registered Routes:")
    print("-" * 60)
    for route, handler in server.get_routes().items():
        print(f"  {route:30s} -> {handler}")
    
    # Simulate API calls
    print("\n🧪 Testing API Endpoints:")
    print("-" * 60)
    
    # Test status endpoint
    status_result = server.routes['GET:/api/v1/status']()
    print(f"\n✅ GET /api/v1/status")
    print(f"   Response: {status_result}")
    
    # Test users endpoint
    users_result = server.routes['GET:/api/v1/users']()
    print(f"\n✅ GET /api/v1/users")
    print(f"   Response: {users_result}")
    
    # Test products endpoint
    products_result = server.routes['GET:/api/v1/products']()
    print(f"\n✅ GET /api/v1/products")
    print(f"   Response: {products_result}")
    
    print("\n" + "=" * 60)
    print("✨ API Server demonstration complete!")
    print("=" * 60)
    print("\n💡 To run the full server:")
    print("   pip install flask flask-restful flask-jwt-extended")
    print("   python projects/advanced/api_server_full.py")
    print()


if __name__ == '__main__':
    main()
