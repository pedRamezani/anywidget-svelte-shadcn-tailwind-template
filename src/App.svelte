<script>
	import './app.css';

	/** @type {{ bindings: { value: number }}}*/
	let { bindings } = $props();
</script>

<button class="w-sm rounded-sm bg-red-500 p-2 text-xl text-red-50" onclick={() => bindings.value++}
	>Count is {bindings.value}</button
>
