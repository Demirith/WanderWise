import { Component, createSignal, onCleanup } from "solid-js";
import { Button } from "solid-bootstrap";
import styles from "./App.module.css";
import { SCREEN_NAV_BAR_WIDTH_LIMIT } from "./constants";

const App: Component = (props: any) => {
  const getNavBarState = () => {
    return SCREEN_NAV_BAR_WIDTH_LIMIT <= window.innerWidth;
  };

  const [shouldShowNav, setShouldShowNav] = createSignal(getNavBarState());
  const [shouldShowOverlay, setShouldShowOverlay] = createSignal(false);

  const handleResize = () => {
    setShouldShowNav(getNavBarState());
  };

  window.addEventListener("resize", handleResize);

  onCleanup(() => {
    window.removeEventListener("resize", handleResize);
  });

  const toggleShowNavigation = () => {
    setShouldShowNav(!shouldShowNav());
    if (shouldShowNav()) {
      setShouldShowOverlay(true);
    } else {
      setShouldShowOverlay(false);
    }
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
      {shouldShowOverlay() && (
        <div class={styles.overlay} onClick={toggleShowNavigation}></div>
      )}
      <nav class={`${shouldShowNav() ? "" : styles.nav__hide}`}>
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
