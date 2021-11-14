<script>
    import { Sveltik, Form } from "sveltik"
    import {goto} from "@roxi/routify"

    import { logout } from "$services/auth"
    import { user } from "$stores/user"

    let onSubmit = async (values, { setSubmitting }) => {
        try {
            await logout()
        } catch (e) {
        } finally {
            setSubmitting(false)
            user.set({isLoggedIn: false})
            $goto("/index")
        }
    }
</script>

<Sveltik {onSubmit} let:isSubmitting>
    <Form role="none">
        <button type="submit"
                disabled={isSubmitting}
                class="block w-full rounded-md border-2 border-red-500 py-2 px-3 text-center text-base font-medium text-red-500 hover:bg-opacity-75" role="menuitem" tabindex="-1">
            {isSubmitting ? "Signing out..." : "Sign out"}
        </button>
    </Form>
</Sveltik>