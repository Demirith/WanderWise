import { Component, createSignal } from "solid-js";
import { Form, Row, Col, Button } from "solid-bootstrap";
import { JSX } from "solid-js/jsx-runtime";

const TripForm: Component = () => {
  const [startDestination, setStartDestination] = createSignal("");
  const [endDestination, setEndDestination] = createSignal("");
  const [duration, setDuration] = createSignal("");
  const [budget, setBudget] = createSignal("");
  const [pointOfInterests, setPointOfInterests] = createSignal("");
  const [interests, setInterests] = createSignal("");

  const handleStartDestinationInputChange: JSX.EventHandler<any, InputEvent> = (
    event
  ) => {
    setStartDestination(event.currentTarget.value);
    console.log("event.currentTarget.value: ", event.currentTarget.value);
  };

  const handleEndDestinationInputChange: JSX.EventHandler<any, InputEvent> = (
    event
  ) => {
    setEndDestination(event.currentTarget.value);
    console.log("event.currentTarget.value: ", event.currentTarget.value);
  };

  const handleDurationInputChange: JSX.EventHandler<any, InputEvent> = (
    event
  ) => {
    setDuration(event.currentTarget.value);
    console.log("event.currentTarget.value: ", event.currentTarget.value);
  };

  const handleBudgetInputChange: JSX.EventHandler<any, InputEvent> = (
    event
  ) => {
    setBudget(event.currentTarget.value);
    console.log("event.currentTarget.value: ", event.currentTarget.value);
  };

  const handlePointOfInterestsInputChange: JSX.EventHandler<any, InputEvent> = (
    event
  ) => {
    setPointOfInterests(event.currentTarget.value);
    console.log("event.currentTarget.value: ", event.currentTarget.value);
  };

  const handleInterestsInputChange: JSX.EventHandler<any, InputEvent> = (
    event
  ) => {
    setInterests(event.currentTarget.value);
    console.log("event.currentTarget.value: ", event.currentTarget.value);
  };

  const handleSubmit = (event: any) => {
    event.preventDefault();
    console.log("Interests:", interests());
    console.log("pointOfInterests:", pointOfInterests());
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Row class="mb-3">
        <Form.Group as={Col} controlId="formGridStartDestination">
          <Form.Label>
            Start Destination: Where will your trip begin?
          </Form.Label>
          <Form.Control
            type="StartDestination"
            placeholder="Start Destination"
            value={startDestination()}
            onInput={handleStartDestinationInputChange}
          />
        </Form.Group>

        <Form.Group as={Col} controlId="formGridEndDestination">
          <Form.Label>End Destination: Where will your trip end?</Form.Label>
          <Form.Control
            type="EndDestination"
            placeholder="End Destination"
            value={endDestination()}
            onInput={handleEndDestinationInputChange}
          />
        </Form.Group>
      </Row>

      <Form.Group class="mb-3" controlId="formGridDuration">
        <Form.Label>How many days will your trip last?</Form.Label>
        <Form.Control
          placeholder="Duration"
          value={duration()}
          onInput={handleDurationInputChange}
        />
      </Form.Group>

      <Form.Group class="mb-3" controlId="formGridBudget">
        <Form.Label>What is your estimated budget for the trip?</Form.Label>
        <Form.Control
          placeholder="Budget"
          value={budget()}
          onInput={handleBudgetInputChange}
        />
      </Form.Group>

      <Form.Group class="mb-3" controlId="formGridPointsOfInterest">
        <Form.Label>
          What specific places or attractions would you like to visit during
          your trip? (e.g., cities, mountains, lakes, landmarks, shops)
        </Form.Label>
        <Form.Control
          placeholder="Points of Interest"
          value={pointOfInterests()}
          onInput={handlePointOfInterestsInputChange}
        />
      </Form.Group>

      <Form.Group class="mb-3" controlId="formGridInterests">
        <Form.Label>
          What activities or experiences are you interested in? (e.g., fishing,
          hiking, shopping, cultural experiences)
        </Form.Label>
        <Form.Control
          placeholder="Interests"
          value={interests()}
          onInput={handleInterestsInputChange}
        />
      </Form.Group>

      <Button variant="primary" type="submit">
        Submit
      </Button>
    </Form>
  );
};

export default TripForm;
