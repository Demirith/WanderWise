import type { Component } from "solid-js";
import { createSignal } from "solid-js";
import { useParams } from "@solidjs/router";
import styles from "./Suggestion.module.css";

const Suggestion: Component = () => {
  const [content, setContent] = createSignal("");
  const params = useParams();

  setContent(decodeURIComponent(params.content) || "");

  return (
    <div class={styles.Suggestion}>
      <h1>Traveling plan</h1>
      <br />
      <p>{content()}</p>
    </div>
  );
};

export default Suggestion;
