import type { Component } from "solid-js";
import styles from "./Home.module.css";

const Home: Component = () => {
  return (
    <div class={styles.Home}>
      <h1>Welcome to Wander Wise!</h1>
      <p>
        Embark on your next adventure with confidence and ease. Whether you're
        planning a solo expedition or a family getaway, Wander Wise is your
        trusted companion for discovering the world's hidden gems.
      </p>
      <ul>
        <li>
          Explore our curated travel suggestions tailored to your interests and
          budget.
        </li>
        <li>
          Plan your itinerary effortlessly with personalized trip
          recommendations.
        </li>
        <li>
          Stay organized with our intuitive trip planning tools, from packing
          lists to daily schedules.
        </li>
      </ul>
      <p>
        Start your journey today and unlock unforgettable experiences around the
        globe!
      </p>
      <p>Happy travels,</p>
      <p>The Wander Wise Team</p>
    </div>
  );
};

export default Home;
