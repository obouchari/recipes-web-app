import axios from "axios";

export async function authenticate(email, password) {
  return await axios.post(
    "/api/login",
    {},
    {
      auth: {
        username: email,
        password,
      },
    }
  );
}

export async function logout() {
  return await axios.post("/api/logout");
}

export async function register(user) {
  return await axios.post("/api/register", user);
}
