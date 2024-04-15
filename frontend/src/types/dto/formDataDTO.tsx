export type FormDataDTO = {
  start_destination: string;
  end_destination: string;
  duration: string;
  budget: string;
  points_of_interest: string;
  interests: string;
};

export function createFormDataDTO(
  startDestination: string,
  endDestination: string,
  duration: string,
  budget: string,
  pointOfInterests: string,
  interests: string
): FormDataDTO {
  return {
    start_destination: startDestination,
    end_destination: endDestination,
    duration: duration,
    budget: budget,
    points_of_interest: pointOfInterests,
    interests: interests,
  };
}
