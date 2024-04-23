import type { Component } from "solid-js";
import styles from "./App.module.css";

const App: Component = (props: any) => {
  return (
    <div class={styles.App}>
      <nav>
        <ul>
          <li>
            <a href="/">Home</a>
          </li>
          <li>
            <a href="/trip">Create trip</a>
          </li>
        </ul>
      </nav>
      <br />
      <main class={styles.main}>{props.children}</main>
    </div>
  );
};

export default App;
