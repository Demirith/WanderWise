import type { Component } from "solid-js";
import styles from "./App.module.css";

const App: Component = (props: any) => {
  return (
    <div class={styles.App}>
      <h1>Wander Wise</h1>
      <nav>
        <a href="/">Home</a>
        <br />
        <a href="/trip">Create suggestion</a>
      </nav>
      <br />
      {props.children}
    </div>
  );
};

export default App;
