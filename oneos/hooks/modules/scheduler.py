from typing import Any, Tuple, Callable, Dict
from random import randint

from oneos.hooks.types.scheduler import (
    # AgentSubmitDeclaration,
    # FactoryParams,
    # LLMParams,
    SchedulerParams,
    # LLMRequestQueue,
    # QueueGetMessage,
    # QueueAddMessage,
    # QueueCheckEmpty,
)

from oneos.hooks.types.llm import LLMRequestQueue
from oneos.hooks.types.memory import MemoryRequestQueue
from oneos.hooks.types.storage import StorageRequestQueue
from oneos.hooks.types.tool import ToolRequestQueue

from contextlib import contextmanager

from oneos.hooks.utils.validate import validate
from oneos.hooks.stores import queue as QueueStore, processes as ProcessStore
from oneos.scheduler.fifo_scheduler import FIFOScheduler
from oneos.scheduler.rr_scheduler import RRScheduler


@validate(SchedulerParams)
def useFIFOScheduler(
    params: SchedulerParams,
):
    """
    Initialize and return a scheduler with start and stop functions.

    Args:
        params (SchedulerParams): Parameters required for the scheduler.

    """
    if params.get_llm_syscall is None:
        from oneos.hooks.stores._global import global_llm_req_queue_get_message
        params.get_llm_syscall = global_llm_req_queue_get_message
        
    if params.get_memory_syscall is None:
        from oneos.hooks.stores._global import global_memory_req_queue_get_message
        params.get_memory_syscall = global_memory_req_queue_get_message
        
    if params.get_storage_syscall is None:
        from oneos.hooks.stores._global import global_storage_req_queue_get_message
        params.get_storage_syscall = global_storage_req_queue_get_message
        
    if params.get_tool_syscall is None:
        from oneos.hooks.stores._global import global_tool_req_queue_get_message
        params.get_tool_syscall = global_tool_req_queue_get_message
    
    # if params.llm_request_queue is None:
    #     params.llm_request_queue = LLMRequestQueue
        
    # if params.memory_request_queue is None:
    #     params.memory_request_queue = MemoryRequestQueue
        
    # if params.storage_request_queue is None:
    #     params.storage_request_queue = StorageRequestQueue
        
    # if params.tool_request_queue is None:
    #     params.tool_request_queue = ToolRequestQueue
    
    scheduler = FIFOScheduler(**params.model_dump())

    # Function to start the scheduler
    def startScheduler():
        scheduler.start()

    # Function to stop the scheduler
    def stopScheduler():
        scheduler.stop()

    return startScheduler, stopScheduler


@contextmanager
@validate(SchedulerParams)
def fifo_scheduler(params: SchedulerParams):
    """
    A context manager that starts and stops a FIFO scheduler.

    Args:
        params (SchedulerParams): The parameters for the scheduler.
    """
    # if params.get_llm_syscall is None:
    #     from oneos.hooks.stores._global import global_llm_req_queue_get_message
    #     params.get_llm_syscall = global_llm_req_queue_get_message

    # if params.get_memory_syscall is None:
    #     from oneos.hooks.stores._global import global_memory_req_queue_get_message
    #     params.get_memory_syscall = global_memory_req_queue_get_message
    
    # if params.get_storage_syscall is None:
    #     from oneos.hooks.stores._global import global_storage_req_queue_get_message
    #     params.get_storage_syscall = global_storage_req_queue_get_message
        
    # if params.get_tool_syscall is None:
    #     from oneos.hooks.stores._global import global_tool_req_queue_get_message
    #     params.get_tool_syscall = global_tool_req_queue_get_message
    
    if params.llm_request_queue is None:
        params.llm_request_queue = LLMRequestQueue
        
    if params.memory_request_queue is None:
        params.memory_request_queue = MemoryRequestQueue
        
    if params.storage_request_queue is None:
        params.storage_request_queue = StorageRequestQueue
        
    if params.tool_request_queue is None:
        params.tool_request_queue = ToolRequestQueue
    
    scheduler = FIFOScheduler(**params.model_dump())

    scheduler.start()
    yield
    scheduler.stop()

@validate(SchedulerParams)
def fifo_scheduler_nonblock(params: SchedulerParams):
    """
    A context manager that starts and stops a FIFO scheduler.

    Args:
        params (SchedulerParams): The parameters for the scheduler.
    """
    if params.get_llm_syscall is None:
        from oneos.hooks.stores._global import global_llm_req_queue_get_message
        params.get_llm_syscall = global_llm_req_queue_get_message

    if params.get_memory_syscall is None:
        from oneos.hooks.stores._global import global_memory_req_queue_get_message
        params.get_memory_syscall = global_memory_req_queue_get_message
    
    if params.get_storage_syscall is None:
        from oneos.hooks.stores._global import global_storage_req_queue_get_message
        params.get_storage_syscall = global_storage_req_queue_get_message
        
    if params.get_tool_syscall is None:
        from oneos.hooks.stores._global import global_tool_req_queue_get_message
        params.get_tool_syscall = global_tool_req_queue_get_message
    
    # if params.llm_request_queue is None:
    #     params.llm_request_queue = LLMRequestQueue
        
    # if params.memory_request_queue is None:
    #     params.memory_request_queue = MemoryRequestQueue
        
    # if params.storage_request_queue is None:
    #     params.storage_request_queue = StorageRequestQueue
        
    # if params.tool_request_queue is None:
    #     params.tool_request_queue = ToolRequestQueue
    
    scheduler = FIFOScheduler(**params.model_dump())

    return scheduler

@validate(SchedulerParams)
def rr_scheduler_nonblock(params: SchedulerParams):
    """
    A context manager that starts and stops a FIFO scheduler.

    Args:
        params (SchedulerParams): The parameters for the scheduler.
    """
    if params.get_llm_syscall is None:
        from oneos.hooks.stores._global import global_llm_req_queue_get_message
        params.get_llm_syscall = global_llm_req_queue_get_message

    if params.get_memory_syscall is None:
        from oneos.hooks.stores._global import global_memory_req_queue_get_message
        params.get_memory_syscall = global_memory_req_queue_get_message
    
    if params.get_storage_syscall is None:
        from oneos.hooks.stores._global import global_storage_req_queue_get_message
        params.get_storage_syscall = global_storage_req_queue_get_message
        
    if params.get_tool_syscall is None:
        from oneos.hooks.stores._global import global_tool_req_queue_get_message
        params.get_tool_syscall = global_tool_req_queue_get_message
    
    # if params.llm_request_queue is None:
    #     params.llm_request_queue = LLMRequestQueue
        
    # if params.memory_request_queue is None:
    #     params.memory_request_queue = MemoryRequestQueue
        
    # if params.storage_request_queue is None:
    #     params.storage_request_queue = StorageRequestQueue
        
    # if params.tool_request_queue is None:
    #     params.tool_request_queue = ToolRequestQueue
    
    scheduler = RRScheduler(**params.model_dump())

    return scheduler