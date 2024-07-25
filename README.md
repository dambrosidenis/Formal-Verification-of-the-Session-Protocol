# Verifying the Security Properties of the Session Protocol in the Symbolic Model with the Tamarin Prover

In recent years, the necessity for robust security in digital communications has become crucial due to the ubiquitous nature of interconnected systems. This thesis focuses on the formal verification of the [Session Messaging App](https://getsession.org), an open-source messaging application designed to offer end-to-end encrypted, anonymous communication through a decentralized network. By utilizing the Tamarin prover, this work aims to rigorously verify the security properties of Session's communication protocol. The study encompasses reverse-engineering the protocol from available source code, formalizing its security properties, and analyzing both peer-to-peer message delivery (abstracting the underlying network) and the onion routing protocol that underpins the infrastructure. The results demonstrate the protocol's adherence to its security specifications within the assumed constraints, providing a comprehensive specification of the protocol and suggesting improvements for future iterations.


## Repository Structure


- `CITATION.cff`: Citation file for referencing this work.
- `LICENSE`: License file for the repository.
- `README.md`: This README file.
- `src/`: Contains the source files for the Tamarin prover theories and custom oracles.
  - `e2e/`: Files related to the end-to-end subprotocol.
    - `e2e.spthy`: Tamarin theory for the e2e protocol.
    - `e2eoracle.py`: Custom oracle script for the e2e theory proofs.
    - `e2epriorities.json`: Support information for the e2e oracle.
  - `onionrouting/`: Files related to verifying the onion routing infrastructure.
    - `onionrouting.spthy`: Tamarin theory for the onion routing protocol.
    - `onionroutingoracle.py`: Custom oracle script for the onion routing proofs.
- `thesis.pdf`: The bachelor thesis document providing detailed information on the theories, implementation, and verification process.

## Getting Started

### Prerequisites

To run the Tamarin prover and the custom oracles, you need to have the following installed:

- [Tamarin Prover](https://tamarin-prover.github.io/) (version 1.6.1 was used for this thesis)
- Python (for running the custom oracles)

### Running the Theories

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. **Navigate to the Source Directory:**

    ```bash
    cd src
    ```

3. **Run the Tamarin Prover on the Theories:**

    For the e2e theory:

    ```bash
    tamarin-prover e2e/e2e.spthy
    ```

    For the onion routing theory:

    ```bash
    tamarin-prover onionrouting/onionrouting.spthy
    ```

## Documentation

For detailed information about the theories, implementation, and verification process, please refer to `thesis.pdf`. This document is the comprehensive source of information and should be the main reference point for understanding and working with the contents of this repository.

## Citation

If you use this repository or find it helpful, please cite it using the information provided in `CITATION.cff`.

## License

This repository is licensed under the terms specified in the `LICENSE` file.

