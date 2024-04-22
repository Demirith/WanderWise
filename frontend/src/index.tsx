/* @refresh reload */
import { render } from "solid-js/web";
import { Router, Route } from "@solidjs/router";
import App from "./App";
import TripForm from "./pages/tripForm/TripForm";
import Home from "./pages/home/Home";
import NotFound from "./pages/notFound/NotFound";
import Suggestion from "./pages/suggestion/Suggestion";
import ErrorPage from "./pages/errorPage/ErrorPage";

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
      <Route path="/suggestion/:content" component={Suggestion} />
      <Route path="*404" component={NotFound} />
      <Route path="/error/:message" component={ErrorPage} />
    </Router>
  ),
  root
);
