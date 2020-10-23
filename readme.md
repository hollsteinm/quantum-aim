# Quantum AIM Sampler

Companion to the "Intro to the Quantum Cloud" Webinar on October 29th, 2020.

Quantum AIM (**A**WS Braket, **I**BM Qiskit, and **M**icrosoft Q#) is a mono repo of examples for similar operations across AWS Braket, Qiskit, and Q#. This is so that people have a one stop shop for comparing and contrasting developer experiences within each of these Software Development Kits (SDKs).

## Getting Started

Pick one of the SDKs you would like to see samples of and navigate to that directory. Each sub-project has a `readme.md` for further instructions. The majority of this project was done within VS Code on Windows; however, any environment in which python and .NET Core 3.1 code can run should be suitable. You can pick whatever IDE best suits you.

## Run All

If you have all pre-requisites as described in their relative readme documents, you can run all projects with the below, lazily written, script:

```bash
cd aws-braket
init
python main.py
deactivate

cd ../ibm-qiskit
init
python main.py
deactivate

cd ../MicrosoftQSharp
dotnet run --shots 1000
cd ../

```
