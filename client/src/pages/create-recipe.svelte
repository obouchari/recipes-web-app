<script>
    import { Sveltik, Form } from "sveltik"
    import {goto, url} from "@roxi/routify"

    import InputField from "$lib/forms/InputField.svelte";
    import {authenticate} from "$services/auth";
    import {user} from "$stores/user";
    import TextArea from "$lib/forms/TextArea.svelte";
    import FileUpload from "$lib/forms/FileUpload.svelte";
    import AutoComplete from "$lib/forms/AutoComplete.svelte";

    let addRecipeError = ""

    let initialValues = {
        name: "",
        description: "",
        instructions: "",
        notes: "",
        duration: 20,
        difficulty: "easy",
        serving: 2,
        category: "",
        tags: [],
        picture: "",
        ingredients: []
    }

    let validate = values => {
        const errors = {}

        // if (!values.email) {
        //     errors.email = "Email is required."
        // }
        //
        // if (!values.password) {
        //     errors.password = "Password is required."
        // }

        return errors
    }

    let onSubmit = async (values, { setSubmitting }) => {
        try {
            // const res = await authenticate(values.email, values.password)
            // user.set({isLoggedIn: true, ...res.data})
            // $goto("/index")
        } catch (e) {
            // addRecipeError = ""
        } finally {
            setSubmitting(false)
        }
    }

    let ingredients = []

    function loadApiData(e) {
        console.log(e)
    }
</script>

<div class="py-6 sm:px-8 md:px-24 lg:px-48">
    <div class="pb-5 mb-8 border-b border-gray-200 sm:flex sm:items-center sm:justify-between">
        <h2 class="text-2xl font-extrabold tracking-tight sm:text-3xl leading-6 text-gray-900">
            Create a recipe
        </h2>
    </div>
<Sveltik {initialValues} {validate} {onSubmit} let:isSubmitting>
    <Form class="space-y-8 divide-y divide-gray-200">
        <div class="space-y-8 divide-y divide-gray-200">
            <div>
                <div>
                    <h3 class="text-lg leading-6 font-medium text-gray-900">Recipe Details</h3>
                    <p class="mt-1 text-sm text-gray-500">
                        The fields marked with an asterisk (*) are required.
                    </p>
                </div>

                <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
                    <div class="sm:col-span-6">
                        <InputField name="name" label="Recipe name*"/>
                    </div>

                    <div class="sm:col-span-6">
                        <TextArea name="description" label="Description*" placeholder="Enter a brief description of your recipe"/>
                    </div>

                    <div class="sm:col-span-3">
                        <div>
                            <label for="category" class="block text-sm font-medium text-gray-700">Category*</label>
                            <select id="category" name="category" class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md">
                                <option value="main-dish" selected>Main Dish</option>
                                <option value="side-dish">Side Dish</option>
                                <option value="appetizer">Appetizer</option>
                                <option value="dessert">Dessert</option>
                                <option value="beverage">Beverage</option>
                                <option value="snack">Snack</option>
                            </select>
                        </div>
                    </div>

                    <div class="sm:col-span-3">
                        <div>
                            <label for="difficulty" class="block text-sm font-medium text-gray-700">Difficulty*</label>
                            <select id="difficulty" name="difficulty" class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md">
                                <option value="easy" selected>Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Complex</option>
                            </select>
                        </div>
                    </div>

                    <div class="sm:col-span-3 sm:col-start-1">
                        <div>
                            <InputField name="duration" label="Duration in Minutes*" type="number" min="1"/>
                            <p class="mt-2 text-sm text-gray-500">Include preparation time.</p>
                        </div>
                    </div>

                    <div class="sm:col-span-3">
                        <div>
                            <InputField name="serving" label="Serving*" type="number" min="1"/>
                            <p class="mt-2 text-sm text-gray-500">How many people it will serve.</p>
                        </div>
                    </div>

                    <div class="sm:col-span-6">
                        <FileUpload name="picture" label="Recipe Photo"/>
                    </div>

                    <div class="sm:col-span-6">
                        <TextArea name="notes" label="Notes" placeholder="Additional notes"/>
                    </div>

<!--                    <div class="sm:col-span-3">-->
<!--                        <InputField name="tags" label="Tags" on:keydown={addTag}/>-->
<!--                    </div>-->

<!--                    <div class="sm:col-span-6">-->

<!--                    </div>-->
                </div>
            </div>

            <div class="pt-8">
                <div>
                    <h3 class="text-lg leading-6 font-medium text-gray-900">
                        Ingredients and Instructions
                    </h3>
                    <p class="mt-1 text-sm text-gray-500">
                        Add recipe ingredients and instructions on how to make it.
                    </p>
                </div>
                <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">

                    <div class="sm:col-span-3">
                        <InputField name="measurement" label="Measurement" placeholder="2 Cups of" />
                    </div>

                    <div class="sm:col-span-3">
                        <div class="flex items-end">
                            <div class="w-full">
                                <AutoComplete name="ingredient" label="Ingredient" placeholder="Milk"/>
                            </div>
                            <button type="button" class="inline-flex items-center ml-2 px-2 py-2 border border-gray-300 shadow-sm text-sm leading-4 font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-yellow-400">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                                </svg>
                            </button>
                        </div>
                        <p class="mt-2 text-sm text-gray-500">Use lower case characters only.</p>
                    </div>

                    <div class="sm:col-span-6">
                        <TextArea name="instructions" label="Instructions" placeholder="Step by step directions on how to make the recipe." rows="5"/>
                    </div>
                </div>
            </div>
        </div>

        <div class="pt-5">
            <div class="flex justify-end">
                <button type="submit" class="ml-3 inline-flex justify-center py-2 px-8 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-red-500 hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
                    Save
                </button>
            </div>
        </div>
    </Form>
</Sveltik>
</div>