import type { Component } from "solid-js";
import { createSignal } from "solid-js";
import { useParams } from "@solidjs/router";

const ErrorPage: Component = () => {
  const [message, setMessage] = createSignal("");
  const params = useParams();

  setMessage(decodeURIComponent(params.message) || "");

  return (
    <div>
      <h1>Error</h1>
      <br />
      <p>{message()}</p>
    </div>
  );
};

export default ErrorPage;
