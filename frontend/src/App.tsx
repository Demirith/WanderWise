import type { Component } from "solid-js";
import TripsForm from "./components/TripForm";
import styles from "./App.module.css";

const App: Component = () => {
  return (
    <div class={styles.App}>
      <TripsForm />
    </div>
  );
};

export default App;
