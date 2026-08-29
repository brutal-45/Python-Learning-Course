"""
Advanced Project: Machine Learning Data Pipeline
================================================

This project demonstrates building a production-ready ML data pipeline.
It covers advanced Python concepts including:
- Generator functions and iterators
- Context managers
- Decorators for timing and logging
- Type hints and data validation
- Async/await patterns
- Data transformation pipelines

Features:
- Lazy data loading with generators
- Pipeline pattern for data transformations
- Performance monitoring
- Error handling and recovery
- Batch processing

Requirements:
    pip install pandas numpy scikit-learn (optional, for full ML features)
"""

import time
import logging
from datetime import datetime
from typing import List, Dict, Any, Callable, Iterator, Optional, TypeVar, Generic
from functools import wraps
from contextlib import contextmanager
from dataclasses import dataclass, field
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# Type variables for generic pipeline
T = TypeVar('T')
R = TypeVar('R')


def timing_decorator(func: Callable) -> Callable:
    """Decorator to measure function execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        logger.info(f"{func.__name__} executed in {elapsed:.4f} seconds")
        return result
    return wrapper


@contextmanager
def pipeline_stage(stage_name: str):
    """Context manager for pipeline stage monitoring"""
    logger.info(f"🚀 Starting stage: {stage_name}")
    start_time = time.time()
    try:
        yield
        elapsed = time.time() - start_time
        logger.info(f"✅ Completed stage: {stage_name} ({elapsed:.2f}s)")
    except Exception as e:
        elapsed = time.time() - start_time
        logger.error(f"❌ Failed stage: {stage_name} after {elapsed:.2f}s - {str(e)}")
        raise


@dataclass
class DataRecord:
    """Represents a single data record"""
    id: int
    features: Dict[str, float]
    label: Optional[int] = None
    timestamp: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'features': self.features,
            'label': self.label,
            'timestamp': self.timestamp.isoformat()
        }


class DataGenerator:
    """
    Generator class for lazy data loading
    
    Demonstrates:
    - Generator functions
    - Memory-efficient data loading
    - Iterator protocol
    """
    
    def __init__(self, n_samples: int = 1000):
        self.n_samples = n_samples
    
    def generate_sample_data(self) -> Iterator[DataRecord]:
        """Generate sample data records lazily"""
        for i in range(self.n_samples):
            record = DataRecord(
                id=i,
                features={
                    'feature_1': float(i % 10),
                    'feature_2': float(i % 7),
                    'feature_3': float(i % 5)
                },
                label=i % 3
            )
            yield record
    
    def batch_generator(self, batch_size: int = 32) -> Iterator[List[DataRecord]]:
        """Generate batches of data"""
        batch = []
        for record in self.generate_sample_data():
            batch.append(record)
            if len(batch) >= batch_size:
                yield batch
                batch = []
        if batch:
            yield batch


class PipelineStep(Generic[T, R]):
    """Generic pipeline step with transform functionality"""
    
    def __init__(self, name: str, transform_func: Callable[[T], R]):
        self.name = name
        self.transform_func = transform_func
    
    @timing_decorator
    def execute(self, data: T) -> R:
        """Execute the transformation"""
        return self.transform_func(data)


class DataPipeline:
    """
    Data Processing Pipeline
    
    Demonstrates:
    - Chain of responsibility pattern
    - Generic type hints
    - Pipeline composition
    """
    
    def __init__(self, name: str = "ML Pipeline"):
        self.name = name
        self.steps: List[PipelineStep] = []
    
    def add_step(self, name: str, transform_func: Callable) -> 'DataPipeline':
        """Add a step to the pipeline"""
        step = PipelineStep(name, transform_func)
        self.steps.append(step)
        return self
    
    @timing_decorator
    def run(self, data: Any) -> Any:
        """Execute all pipeline steps sequentially"""
        logger.info(f"Running pipeline: {self.name}")
        result = data
        
        for step in self.steps:
            with pipeline_stage(step.name):
                result = step.execute(result)
        
        logger.info(f"Pipeline {self.name} completed successfully")
        return result


def create_sample_pipeline() -> DataPipeline:
    """Create a sample data processing pipeline"""
    
    def normalize_features(data: List[DataRecord]) -> List[DataRecord]:
        """Normalize feature values"""
        for record in data:
            max_val = max(record.features.values()) or 1
            record.features = {k: v/max_val for k, v in record.features.items()}
        return data
    
    def filter_outliers(data: List[DataRecord]) -> List[DataRecord]:
        """Filter out outlier records"""
        return [r for r in data if sum(r.features.values()) < 20]
    
    def add_metadata(data: List[DataRecord]) -> List[DataRecord]:
        """Add metadata to records"""
        for record in data:
            record.features['record_count'] = len(data)
        return data
    
    pipeline = DataPipeline("Sample ML Pipeline")
    pipeline.add_step("Normalize Features", normalize_features)
    pipeline.add_step("Filter Outliers", filter_outliers)
    pipeline.add_step("Add Metadata", add_metadata)
    
    return pipeline


def main():
    """Main entry point demonstrating the ML pipeline"""
    print("=" * 60)
    print("Advanced Project: ML Data Pipeline")
    print("=" * 60)
    
    # Create data generator
    generator = DataGenerator(n_samples=100)
    
    # Load first batch of data
    print("\n📊 Loading sample data...")
    data_batch = next(generator.batch_generator(batch_size=10))
    print(f"   Loaded {len(data_batch)} records")
    
    # Display sample record
    print("\n📋 Sample Record:")
    print(f"   {json.dumps(data_batch[0].to_dict(), indent=2)}")
    
    # Create and run pipeline
    print("\n⚙️  Creating data processing pipeline...")
    pipeline = create_sample_pipeline()
    
    # Execute pipeline
    print("\n🔄 Running pipeline...")
    processed_data = pipeline.run(data_batch)
    
    # Display results
    print(f"\n✅ Processed {len(processed_data)} records")
    print("\n📋 Processed Sample Record:")
    print(f"   {json.dumps(processed_data[0].to_dict(), indent=2)}")
    
    # Demonstrate async-style processing
    print("\n⚡ Demonstrating batch processing...")
    total_processed = 0
    for batch in generator.batch_generator(batch_size=20):
        processed = pipeline.run(batch)
        total_processed += len(processed)
    
    print(f"\n✨ Total records processed: {total_processed}")
    
    print("\n" + "=" * 60)
    print("ML Pipeline demonstration complete!")
    print("=" * 60)
    print("\n💡 To extend this pipeline:")
    print("   - Add database connectors")
    print("   - Integrate with scikit-learn models")
    print("   - Add distributed processing with Dask/Spark")
    print()


if __name__ == '__main__':
    main()
