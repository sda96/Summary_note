?	j?t???j?t???!j?t???	;6??F?1@;6??F?1@!;6??F?1@"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$j?t???_?Q???AΈ?????Y[????<??*	fffff?e@2F
Iterator::Model+??????![???F@);pΈ?ް?12?F?NC@:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate+??Χ?!]?????:@)?MbX9??1pv_?=?6@:Preprocessing2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat/n????!?????a4@)V-???1?6p???0@:Preprocessing2U
Iterator::Model::ParallelMapV2??@??ǈ?!?^???@)??@??ǈ?1?^???@:Preprocessing2Z
#Iterator::Model::ParallelMapV2::Zip c?ZB>??!??m?jK@)a2U0*???1:??.<@:Preprocessing2?
OIterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate[0]::TensorSlicey?&1?|?!??}Ҍ6@)y?&1?|?1??}Ҍ6@:Preprocessing2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensora??+ey?!d??+g?@)a??+ey?1d??+g?@:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMapx$(~???!ذi???<@)_?Q?k?1??????:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
both?Your program is MODERATELY input-bound because 17.6% of the total step time sampled is waiting for input. Therefore, you would need to reduce both the input time and other time.no*high2t24.8 % of the total step time sampled is spent on 'All Others' time. This could be due to Python execution overhead.9;6??F?1@>Look at Section 3 for the breakdown of input time on the host.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	_?Q???_?Q???!_?Q???      ??!       "      ??!       *      ??!       2	Έ?????Έ?????!Έ?????:      ??!       B      ??!       J	[????<??[????<??![????<??R      ??!       Z	[????<??[????<??![????<??JCPU_ONLYY;6??F?1@b Y      Y@qt ?l?X@"?	
both?Your program is MODERATELY input-bound because 17.6% of the total step time sampled is waiting for input. Therefore, you would need to reduce both the input time and other time.b
`input_pipeline_analyzer (especially Section 3 for the breakdown of input operations on the Host)m
ktrace_viewer (look at the activities on the timeline of each Host Thread near the bottom of the trace view)"T
Rtensorflow_stats (identify the time-consuming operations executed on the CPU_ONLY)"Z
Xtrace_viewer (look at the activities on the timeline of each CPU_ONLY in the trace view)*?
?<a href="https://www.tensorflow.org/guide/data_performance_analysis" target="_blank">Analyze tf.data performance with the TF Profiler</a>*y
w<a href="https://www.tensorflow.org/guide/data_performance" target="_blank">Better performance with the tf.data API</a>2?
=type.googleapis.com/tensorflow.profiler.GenericRecommendation?
nohigh"t24.8 % of the total step time sampled is spent on 'All Others' time. This could be due to Python execution overhead.:
Refer to the TF2 Profiler FAQb?99.5379% of Op time on the host used eager execution. Performance could be improved with <a href="https://www.tensorflow.org/guide/function" target="_blank">tf.function.</a>2"CPU: B 