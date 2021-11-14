<script>
    import {onMount} from "svelte"
    import { goto } from "@roxi/routify"

    import { user } from "$stores/user"

    let show = false
    let isLoggedIn

    user.subscribe(user => {
        isLoggedIn = user.isLoggedIn
    })

    onMount(() => {
        if (isLoggedIn) {
            show = true
        } else {
            $goto('/login')
        }
    })
</script>

{#if show}
    <slot />
{/if}