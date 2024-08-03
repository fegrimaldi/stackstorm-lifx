# StackStorm LifX

StackStorm LifX allows you to automate your LifX lights with stackstorm.

## Repository Structure

The repository consists of the following components:

- **`actions/`**: This directory contains specific actions implemented using the base action classes defined in `lib/action.py`.
  - `set_scene.py`: Sets the desired scene. Requires color in HSBK format and brightness as a percentage as input parameters.
  - `site_survey.py`: Surveys a site. Useful for gathering data to populate the `lifx.yaml` configuration file. 


- **`actions/lib/`**: This directory contains the base action. It includes the following files:
  - `action`: Defines base action classes that serve as foundations for implementing specific actions related to light functions. Loads configuration data and initializes lights.
  - `utils`: Defines a Light Device Class for use in the site survey.

- **`actions/workflows`**: Workflows
  - `set_daylight`: Sets the lights to bright sunshine.
  - `set_evening`: Sets the lights to a warm, candlelit vibe. 
  - `set_theatre`: Sets the lights a dimly lit red optimzed for viewing movies.

- **`rules`**: Rules (triggers)
  - `none`: Plans to add trigger to align with Astral sensors.
  
- **`README.md`**: This file provides an overview of the repository and its contents.

- **`LICENSE`**: This repository is licensed under the Apache-2 terms.

## Prerequisites

No prerequisites.


## Getting Started

To install the pack, install the prerequisites then follow this step:

1. Install the pack and required dependencies:

    `st2 pack install https://github.com/fegrimaldi/stackstorm-lifx.git`

2. Use the provided actions or extend them to suit your specific use case.

## Contributing

Contributions to Silverwolf Networks are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.

---

Copyright 2024 Silver Wolf Technology - Developed by Fabricio Grimaldi.
