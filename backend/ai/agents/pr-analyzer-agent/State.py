from typing import List, Literal
from pydantic import BaseModel

class FileInsight(BaseModel):
    filename: str
    change_type: Literal['added', 'modified', 'deleted']
    additions: int
    deletions: int
    highlights: List[str]

class Stats(BaseModel):
    files_changed: int
    additions: int
    deletions: int  

class Insights(BaseModel):
    summary: str
    stats: Stats
    files: List[FileInsight]
    risks: List[str]
    recommendations: List[str]
    tags: List[str]

class AnalyzerAgent(BaseModel):
    diff: str
    analyzed_diff: Insights
    summary: str  
