export async function load({ fetch }) {
  const url = `http://127.0.0.1:5000/api/recipes`;
  const res = await fetch(url);

  if (res.ok) {
    return {
      props: {
        recipes: await res.json(),
      },
    };
  }

  return {
    status: res.status,
    error: new Error(`Could not load ${url}`),
  };
}
