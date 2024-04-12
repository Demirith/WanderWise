/* @refresh reload */
import { render } from "solid-js/web";
import { Router, Route } from "@solidjs/router";
import App from "./App";
import TripForm from "./pages/TripForm";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";
import Suggestion from "./pages/Suggestion";

const root = document.getElementById("root");

if (!root || (import.meta.env.DEV && !(root instanceof HTMLElement))) {
  throw new Error(
    "Root element not found. Did you forget to add it to your index.html? Or maybe the id attribute got misspelled?"
  );
}

render(
  () => (
    <Router root={App}>
      <Route path="/" component={Home} />
      <Route path="/trip" component={TripForm} />
      <Route path="/suggestion" component={Suggestion} />
      <Route path="*404" component={NotFound} />
    </Router>
  ),
  root
);
