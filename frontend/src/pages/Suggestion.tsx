import type { Component } from "solid-js";
import { createSignal } from "solid-js";
import { useParams } from "@solidjs/router";

const Suggestion: Component = () => {
  const [content, setContent] = createSignal("");
  const params = useParams();

  setContent(decodeURIComponent(params.content) || "");

  return (
    <div>
      <h1>Suggestion traveling plan</h1>
      <br />
      <p style={{ "white-space": "pre-wrap" }}>{content()}</p>
    </div>
  );
};

export default Suggestion;
