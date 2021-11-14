<script>
	import { url, isActive } from '@roxi/routify'

	export let name
	export let path
	export let onClick = () => {}

	const activeClasses = "bg-gray-300";
</script>


<a href={$url(path)}
   class="{$isActive(path) && activeClasses} text-gray-800 block text-base py-2 px-6 text-sm font-medium focus:outline-none"
   aria-current="page"
   on:click={onClick}>
	{name}
</a>
