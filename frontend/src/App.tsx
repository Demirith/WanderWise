import { Component, createSignal } from "solid-js";
import { Button } from "solid-bootstrap";
import styles from "./App.module.css";

const App: Component = (props: any) => {
  const [shouldShowNav, setShouldShowNav] = createSignal(true);

  const toggleShowNavigation = () => {
    const showNav = shouldShowNav();
    setShouldShowNav(!showNav);
  };

  return (
    <div class={styles.App}>
      <Button
        class={styles.App__button}
        variant="outline-dark"
        onClick={toggleShowNavigation}
      >
        Nav
      </Button>
      {!shouldShowNav() && (
        <div class={styles.overlay} onClick={toggleShowNavigation}></div>
      )}
      <nav class={`${shouldShowNav() ? styles.nav__hide : ""}`}>
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
