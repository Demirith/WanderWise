import { Component, createSignal } from "solid-js";
import { Form, Row, Col, Button } from "solid-bootstrap";
import { JSX } from "solid-js/jsx-runtime";
import { action, useAction, useSubmission, redirect } from "@solidjs/router";
import { createFormDataDTO } from "../types/dto/formDataDTO";
import { FormDataDTO } from "../types/dto/formDataDTO";

const submitFormData = action(async (data: FormDataDTO) => {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/trips/suggestion", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error("Failed to submit form data");
    }

    const responseData = await response.json();
    console.log("responseData.content: ", responseData.content);

    return responseData;
  } catch (error) {
    console.error("Error submitting form data:", error);
    throw error;
  }
});

const TripForm: Component = () => {
  const [startDestination, setStartDestination] = createSignal("Tokoy");
  const [endDestination, setEndDestination] = createSignal("Tokyo");
  const [duration, setDuration] = createSignal("4 weeks");
  const [budget, setBudget] = createSignal("70000 kr");
  const [pointOfInterests, setPointOfInterests] = createSignal("mount fuji");
  const [interests, setInterests] = createSignal("fishing, hiking");

  const handleSubmit = useAction(submitFormData);
  const response = useSubmission(submitFormData);

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

  const handleFormSubmit = (event: Event) => {
    event.preventDefault();

    const data = createFormDataDTO(
      startDestination(),
      endDestination(),
      duration(),
      budget(),
      pointOfInterests(),
      interests()
    );

    handleSubmit(data);
  };

  return (
    <Form onSubmit={handleFormSubmit}>
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
