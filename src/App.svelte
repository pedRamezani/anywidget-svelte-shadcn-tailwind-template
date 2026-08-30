<script lang="ts">
	import { Button } from '$lib/components/ui/button/index';
	import { PlusIcon } from '@lucide/svelte';
	import './app.css';

	let { bindings }: { bindings: { value: number } } = $props();
</script>

<!--
	The widget needs a root element carrying this id: app.css scopes the theme to
	it so the styles cannot leak into the host notebook. Rename it here and in
	app.css together, and keep the whole widget inside it.
-->
<div id="ipyfoo-widget" class="w-full bg-background p-4">
	<Button onclick={() => bindings.value++}>
		<PlusIcon />
		Count is {bindings.value}
	</Button>
</div>
