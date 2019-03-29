# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/tasks_v2/proto/queue.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.tasks_v2.proto import (
    target_pb2 as google_dot_cloud_dot_tasks__v2_dot_proto_dot_target__pb2,
)
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/tasks_v2/proto/queue.proto",
    package="google.cloud.tasks.v2",
    syntax="proto3",
    serialized_options=_b(
        "\n\031com.google.cloud.tasks.v2B\nQueueProtoP\001Z:google.golang.org/genproto/googleapis/cloud/tasks/v2;tasks"
    ),
    serialized_pb=_b(
        '\n\'google/cloud/tasks_v2/proto/queue.proto\x12\x15google.cloud.tasks.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/tasks_v2/proto/target.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xff\x02\n\x05Queue\x12\x0c\n\x04name\x18\x01 \x01(\t\x12L\n\x1b\x61pp_engine_routing_override\x18\x02 \x01(\x0b\x32\'.google.cloud.tasks.v2.AppEngineRouting\x12\x36\n\x0brate_limits\x18\x03 \x01(\x0b\x32!.google.cloud.tasks.v2.RateLimits\x12\x38\n\x0cretry_config\x18\x04 \x01(\x0b\x32".google.cloud.tasks.v2.RetryConfig\x12\x31\n\x05state\x18\x05 \x01(\x0e\x32".google.cloud.tasks.v2.Queue.State\x12.\n\npurge_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\x0c\n\x08\x44ISABLED\x10\x03"j\n\nRateLimits\x12!\n\x19max_dispatches_per_second\x18\x01 \x01(\x01\x12\x16\n\x0emax_burst_size\x18\x02 \x01(\x05\x12!\n\x19max_concurrent_dispatches\x18\x03 \x01(\x05"\xd1\x01\n\x0bRetryConfig\x12\x14\n\x0cmax_attempts\x18\x01 \x01(\x05\x12\x35\n\x12max_retry_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12.\n\x0bmin_backoff\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12.\n\x0bmax_backoff\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x15\n\rmax_doublings\x18\x05 \x01(\x05\x42\x65\n\x19\x63om.google.cloud.tasks.v2B\nQueueProtoP\x01Z:google.golang.org/genproto/googleapis/cloud/tasks/v2;tasksb\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_tasks__v2_dot_proto_dot_target__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)


_QUEUE_STATE = _descriptor.EnumDescriptor(
    name="State",
    full_name="google.cloud.tasks.v2.Queue.State",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="STATE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="RUNNING", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="PAUSED", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DISABLED", index=3, number=3, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=545,
    serialized_end=614,
)
_sym_db.RegisterEnumDescriptor(_QUEUE_STATE)


_QUEUE = _descriptor.Descriptor(
    name="Queue",
    full_name="google.cloud.tasks.v2.Queue",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.tasks.v2.Queue.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="app_engine_routing_override",
            full_name="google.cloud.tasks.v2.Queue.app_engine_routing_override",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="rate_limits",
            full_name="google.cloud.tasks.v2.Queue.rate_limits",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="retry_config",
            full_name="google.cloud.tasks.v2.Queue.retry_config",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="state",
            full_name="google.cloud.tasks.v2.Queue.state",
            index=4,
            number=5,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="purge_time",
            full_name="google.cloud.tasks.v2.Queue.purge_time",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_QUEUE_STATE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=231,
    serialized_end=614,
)


_RATELIMITS = _descriptor.Descriptor(
    name="RateLimits",
    full_name="google.cloud.tasks.v2.RateLimits",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="max_dispatches_per_second",
            full_name="google.cloud.tasks.v2.RateLimits.max_dispatches_per_second",
            index=0,
            number=1,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="max_burst_size",
            full_name="google.cloud.tasks.v2.RateLimits.max_burst_size",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="max_concurrent_dispatches",
            full_name="google.cloud.tasks.v2.RateLimits.max_concurrent_dispatches",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=616,
    serialized_end=722,
)


_RETRYCONFIG = _descriptor.Descriptor(
    name="RetryConfig",
    full_name="google.cloud.tasks.v2.RetryConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="max_attempts",
            full_name="google.cloud.tasks.v2.RetryConfig.max_attempts",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="max_retry_duration",
            full_name="google.cloud.tasks.v2.RetryConfig.max_retry_duration",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="min_backoff",
            full_name="google.cloud.tasks.v2.RetryConfig.min_backoff",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="max_backoff",
            full_name="google.cloud.tasks.v2.RetryConfig.max_backoff",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="max_doublings",
            full_name="google.cloud.tasks.v2.RetryConfig.max_doublings",
            index=4,
            number=5,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=725,
    serialized_end=934,
)

_QUEUE.fields_by_name[
    "app_engine_routing_override"
].message_type = (
    google_dot_cloud_dot_tasks__v2_dot_proto_dot_target__pb2._APPENGINEROUTING
)
_QUEUE.fields_by_name["rate_limits"].message_type = _RATELIMITS
_QUEUE.fields_by_name["retry_config"].message_type = _RETRYCONFIG
_QUEUE.fields_by_name["state"].enum_type = _QUEUE_STATE
_QUEUE.fields_by_name[
    "purge_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_QUEUE_STATE.containing_type = _QUEUE
_RETRYCONFIG.fields_by_name[
    "max_retry_duration"
].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_RETRYCONFIG.fields_by_name[
    "min_backoff"
].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_RETRYCONFIG.fields_by_name[
    "max_backoff"
].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name["Queue"] = _QUEUE
DESCRIPTOR.message_types_by_name["RateLimits"] = _RATELIMITS
DESCRIPTOR.message_types_by_name["RetryConfig"] = _RETRYCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Queue = _reflection.GeneratedProtocolMessageType(
    "Queue",
    (_message.Message,),
    dict(
        DESCRIPTOR=_QUEUE,
        __module__="google.cloud.tasks_v2.proto.queue_pb2",
        __doc__="""A queue is a container of related tasks. Queues are configured to manage
  how those tasks are dispatched. Configurable properties include rate
  limits, retry options, queue types, and others.
  
  
  Attributes:
      name:
          Caller-specified and required in
          [CreateQueue][google.cloud.tasks.v2.CloudTasks.CreateQueue],
          after which it becomes output only.  The queue name.  The
          queue name must have the following format:
          ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID``
          -  ``PROJECT_ID`` can contain letters ([A-Za-z]), numbers
          ([0-9]),    hyphens (-), colons (:), or periods (.). For more
          information, see    `Identifying    projects
          <https://cloud.google.com/resource-manager/docs/creating-
          managing-projects#identifying_projects>`_ -  ``LOCATION_ID``
          is the canonical ID for the queue's location. The    list of
          available locations can be obtained by calling    [ListLocatio
          ns][google.cloud.location.Locations.ListLocations]. For
          more information, see
          https://cloud.google.com/about/locations/. -  ``QUEUE_ID`` can
          contain letters ([A-Za-z]), numbers ([0-9]), or    hyphens
          (-). The maximum length is 100 characters.
      app_engine_routing_override:
          Overrides for [task-level app\_engine\_routing][google.cloud.t
          asks.v2.AppEngineHttpRequest.app\_engine\_routing]. These
          settings apply only to [App Engine
          tasks][google.cloud.tasks.v2.AppEngineHttpRequest] in this
          queue.  If set, ``app_engine_routing_override`` is used for
          all [App Engine
          tasks][google.cloud.tasks.v2.AppEngineHttpRequest] in the
          queue, no matter what the setting is for the [task-level app\_
          engine\_routing][google.cloud.tasks.v2.AppEngineHttpRequest.ap
          p\_engine\_routing].
      rate_limits:
          Rate limits for task dispatches.
          [rate\_limits][google.cloud.tasks.v2.Queue.rate\_limits] and
          [retry\_config][google.cloud.tasks.v2.Queue.retry\_config] are
          related because they both control task attempts. However they
          control task attempts in different ways:  -
          [rate\_limits][google.cloud.tasks.v2.Queue.rate\_limits]
          controls the    total rate of dispatches from a queue (i.e.
          all traffic dispatched    from the queue, regardless of
          whether the dispatch is from a first    attempt or a retry). -
          [retry\_config][google.cloud.tasks.v2.Queue.retry\_config]
          controls    what happens to particular a task after its first
          attempt fails. That    is,
          [retry\_config][google.cloud.tasks.v2.Queue.retry\_config]
          controls task retries (the second attempt, third attempt,
          etc).  The queue's actual dispatch rate is the result of:  -
          Number of tasks in the queue -  User-specified throttling:
          [rate\_limits][google.cloud.tasks.v2.Queue.rate\_limits],
          [retry\_config][google.cloud.tasks.v2.Queue.retry\_config],
          and the    [queue's state][google.cloud.tasks.v2.Queue.state].
          -  System throttling due to ``429`` (Too Many Requests) or
          ``503``    (Service Unavailable) responses from the worker,
          high error rates, or    to smooth sudden large traffic spikes.
      retry_config:
          Settings that determine the retry behavior.  -  For tasks
          created using Cloud Tasks: the queue-level retry settings
          apply to all tasks in the queue that were created using Cloud
          Tasks.    Retry settings cannot be set on individual tasks. -
          For tasks created using the App Engine SDK: the queue-level
          retry    settings apply to all tasks in the queue which do not
          have retry    settings explicitly set on the task and were
          created by the App    Engine SDK. See `App Engine
          documentation <https://cloud.google.com/appengine/docs/standar
          d/python/taskqueue/push/retrying-tasks>`_.
      state:
          Output only. The state of the queue.  ``state`` can only be
          changed by called
          [PauseQueue][google.cloud.tasks.v2.CloudTasks.PauseQueue],
          [ResumeQueue][google.cloud.tasks.v2.CloudTasks.ResumeQueue],
          or uploading `queue.yaml/xml <https://cloud.google.com/appengi
          ne/docs/python/config/queueref>`_.
          [UpdateQueue][google.cloud.tasks.v2.CloudTasks.UpdateQueue]
          cannot be used to change ``state``.
      purge_time:
          Output only. The last time this queue was purged.  All tasks
          that were [created][google.cloud.tasks.v2.Task.create\_time]
          before this time were purged.  A queue can be purged using
          [PurgeQueue][google.cloud.tasks.v2.CloudTasks.PurgeQueue], the
          `App Engine Task Queue SDK, or the Cloud Console <https://clou
          d.google.com/appengine/docs/standard/python/taskqueue/push/del
          eting-tasks-and-queues#purging_all_tasks_from_a_queue>`_.
          Purge time will be truncated to the nearest microsecond. Purge
          time will be unset if the queue has never been purged.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.tasks.v2.Queue)
    ),
)
_sym_db.RegisterMessage(Queue)

RateLimits = _reflection.GeneratedProtocolMessageType(
    "RateLimits",
    (_message.Message,),
    dict(
        DESCRIPTOR=_RATELIMITS,
        __module__="google.cloud.tasks_v2.proto.queue_pb2",
        __doc__="""Rate limits.
  
  This message determines the maximum rate that tasks can be dispatched by
  a queue, regardless of whether the dispatch is a first task attempt or a
  retry.
  
  Note: The debugging command,
  [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask], will run a task
  even if the queue has reached its
  [RateLimits][google.cloud.tasks.v2.RateLimits].
  
  
  Attributes:
      max_dispatches_per_second:
          The maximum rate at which tasks are dispatched from this
          queue.  If unspecified when the queue is created, Cloud Tasks
          will pick the default.  -  For [App Engine
          queues][google.cloud.tasks.v2.AppEngineHttpQueue],    the
          maximum allowed value is 500.  This field has the same meaning
          as `rate in queue.yaml/xml <https://cloud.google.com/appengine
          /docs/standard/python/config/queueref#rate>`_.
      max_burst_size:
          Output only. The max burst size.  Max burst size limits how
          fast tasks in queue are processed when many tasks are in the
          queue and the rate is high. This field allows the queue to
          have a high rate so processing starts shortly after a task is
          enqueued, but still limits resource usage when many tasks are
          enqueued in a short period of time.  The `token bucket
          <https://wikipedia.org/wiki/Token_Bucket>`_ algorithm is used
          to control the rate of task dispatches. Each queue has a token
          bucket that holds tokens, up to the maximum specified by
          ``max_burst_size``. Each time a task is dispatched, a token is
          removed from the bucket. Tasks will be dispatched until the
          queue's bucket runs out of tokens. The bucket will be
          continuously refilled with new tokens based on [max\_dispatche
          s\_per\_second][google.cloud.tasks.v2.RateLimits.max\_dispatch
          es\_per\_second].  Cloud Tasks will pick the value of
          ``max_burst_size`` based on the value of [max\_dispatches\_per
          \_second][google.cloud.tasks.v2.RateLimits.max\_dispatches\_pe
          r\_second].  For App Engine queues that were created or
          updated using ``queue.yaml/xml``, ``max_burst_size`` is equal
          to `bucket\_size <https://cloud.google.com/appengine/docs/stan
          dard/python/config/queueref#bucket_size>`_. Since
          ``max_burst_size`` is output only, if
          [UpdateQueue][google.cloud.tasks.v2.CloudTasks.UpdateQueue] is
          called on a queue created by ``queue.yaml/xml``,
          ``max_burst_size`` will be reset based on the value of [max\_d
          ispatches\_per\_second][google.cloud.tasks.v2.RateLimits.max\_
          dispatches\_per\_second], regardless of whether [max\_dispatch
          es\_per\_second][google.cloud.tasks.v2.RateLimits.max\_dispatc
          hes\_per\_second] is updated.
      max_concurrent_dispatches:
          The maximum number of concurrent tasks that Cloud Tasks allows
          to be dispatched for this queue. After this threshold has been
          reached, Cloud Tasks stops dispatching tasks until the number
          of concurrent requests decreases.  If unspecified when the
          queue is created, Cloud Tasks will pick the default.  The
          maximum allowed value is 5,000.  This field has the same
          meaning as `max\_concurrent\_requests in queue.yaml/xml <https
          ://cloud.google.com/appengine/docs/standard/python/config/queu
          eref#max_concurrent_requests>`_.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.tasks.v2.RateLimits)
    ),
)
_sym_db.RegisterMessage(RateLimits)

RetryConfig = _reflection.GeneratedProtocolMessageType(
    "RetryConfig",
    (_message.Message,),
    dict(
        DESCRIPTOR=_RETRYCONFIG,
        __module__="google.cloud.tasks_v2.proto.queue_pb2",
        __doc__="""Retry config.
  
  These settings determine when a failed task attempt is retried.
  
  
  Attributes:
      max_attempts:
          Number of attempts per task.  Cloud Tasks will attempt the
          task ``max_attempts`` times (that is, if the first attempt
          fails, then there will be ``max_attempts - 1`` retries). Must
          be >= -1.  If unspecified when the queue is created, Cloud
          Tasks will pick the default.  -1 indicates unlimited attempts.
          This field has the same meaning as `task\_retry\_limit in
          queue.yaml/xml <https://cloud.google.com/appengine/docs/standa
          rd/python/config/queueref#retry_parameters>`_.
      max_retry_duration:
          If positive, ``max_retry_duration`` specifies the time limit
          for retrying a failed task, measured from when the task was
          first attempted. Once ``max_retry_duration`` time has passed
          *and* the task has been attempted [max\_attempts][google.cloud
          .tasks.v2.RetryConfig.max\_attempts] times, no further
          attempts will be made and the task will be deleted.  If zero,
          then the task age is unlimited.  If unspecified when the queue
          is created, Cloud Tasks will pick the default.
          ``max_retry_duration`` will be truncated to the nearest
          second.  This field has the same meaning as `task\_age\_limit
          in queue.yaml/xml <https://cloud.google.com/appengine/docs/sta
          ndard/python/config/queueref#retry_parameters>`_.
      min_backoff:
          A task will be
          [scheduled][google.cloud.tasks.v2.Task.schedule\_time] for
          retry between
          [min\_backoff][google.cloud.tasks.v2.RetryConfig.min\_backoff]
          and
          [max\_backoff][google.cloud.tasks.v2.RetryConfig.max\_backoff]
          duration after it fails, if the queue's
          [RetryConfig][google.cloud.tasks.v2.RetryConfig] specifies
          that the task should be retried.  If unspecified when the
          queue is created, Cloud Tasks will pick the default.
          ``min_backoff`` will be truncated to the nearest second.  This
          field has the same meaning as `min\_backoff\_seconds in
          queue.yaml/xml <https://cloud.google.com/appengine/docs/standa
          rd/python/config/queueref#retry_parameters>`_.
      max_backoff:
          A task will be
          [scheduled][google.cloud.tasks.v2.Task.schedule\_time] for
          retry between
          [min\_backoff][google.cloud.tasks.v2.RetryConfig.min\_backoff]
          and
          [max\_backoff][google.cloud.tasks.v2.RetryConfig.max\_backoff]
          duration after it fails, if the queue's
          [RetryConfig][google.cloud.tasks.v2.RetryConfig] specifies
          that the task should be retried.  If unspecified when the
          queue is created, Cloud Tasks will pick the default.
          ``max_backoff`` will be truncated to the nearest second.  This
          field has the same meaning as `max\_backoff\_seconds in
          queue.yaml/xml <https://cloud.google.com/appengine/docs/standa
          rd/python/config/queueref#retry_parameters>`_.
      max_doublings:
          The time between retries will double ``max_doublings`` times.
          A task's retry interval starts at [min\_backoff][google.cloud.
          tasks.v2.RetryConfig.min\_backoff], then doubles
          ``max_doublings`` times, then increases linearly, and finally
          retries retries at intervals of
          [max\_backoff][google.cloud.tasks.v2.RetryConfig.max\_backoff]
          up to [max\_attempts][google.cloud.tasks.v2.RetryConfig.max\_a
          ttempts] times.  For example, if
          [min\_backoff][google.cloud.tasks.v2.RetryConfig.min\_backoff]
          is 10s,
          [max\_backoff][google.cloud.tasks.v2.RetryConfig.max\_backoff]
          is 300s, and ``max_doublings`` is 3, then the a task will
          first be retried in 10s. The retry interval will double three
          times, and then increase linearly by 2^3 \* 10s. Finally, the
          task will retry at intervals of
          [max\_backoff][google.cloud.tasks.v2.RetryConfig.max\_backoff]
          until the task has been attempted [max\_attempts][google.cloud
          .tasks.v2.RetryConfig.max\_attempts] times. Thus, the requests
          will retry at 10s, 20s, 40s, 80s, 160s, 240s, 300s, 300s, ....
          If unspecified when the queue is created, Cloud Tasks will
          pick the default.  This field has the same meaning as
          `max\_doublings in queue.yaml/xml <https://cloud.google.com/ap
          pengine/docs/standard/python/config/queueref#retry_parameters>`__.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.tasks.v2.RetryConfig)
    ),
)
_sym_db.RegisterMessage(RetryConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
