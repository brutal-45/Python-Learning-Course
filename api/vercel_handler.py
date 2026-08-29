from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sys
import os

# Add parent directory to path to import lessons
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                'status': 'healthy',
                'message': 'Python Learning API is running',
                'version': '1.0.0'
            }
            self.wfile.write(json.dumps(response).encode())
        
        elif self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            # Count lesson files
            lessons_dir = os.path.join(os.path.dirname(__file__), '..', 'lessons')
            lesson_count = 0
            if os.path.exists(lessons_dir):
                lesson_count = len([f for f in os.listdir(lessons_dir) if f.endswith('.py')])
            
            # Count project files
            projects_dir = os.path.join(os.path.dirname(__file__), '..', 'projects')
            project_count = 0
            if os.path.exists(projects_dir):
                project_count = len([f for f in os.listdir(projects_dir) if f.endswith('.py')])
            
            response = {
                'status': 'operational',
                'lessons_count': lesson_count,
                'projects_count': project_count,
                'python_version': sys.version
            }
            self.wfile.write(json.dumps(response).encode())
        
        elif self.path.startswith('/api/lessons'):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            lessons = []
            lessons_dir = os.path.join(os.path.dirname(__file__), '..', 'lessons')
            if os.path.exists(lessons_dir):
                for f in sorted(os.listdir(lessons_dir)):
                    if f.endswith('.py'):
                        lessons.append({
                            'name': f[:-3],
                            'file': f
                        })
            
            response = {'lessons': lessons}
            self.wfile.write(json.dumps(response).encode())
        
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'error': 'Not found', 'path': self.path}
            self.wfile.write(json.dumps(response).encode())
