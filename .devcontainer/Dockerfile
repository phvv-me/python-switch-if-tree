ARG VARIANT=3
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

ENV PYTHONUNBUFFERED 1

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# change ls colors for root
RUN export SNIPPET="\nexport LS_OPTIONS='--color=auto'\neval \"\`dircolors\`\"\nalias ls='ls \$LS_OPTIONS'\nalias ll='ls \$LS_OPTIONS -l'\nalias l='ls \$LS_OPTIONS -lA'\n" \
    && echo "$SNIPPET" | tee -a ~/.bashrc \
    && echo "$SNIPPET" | tee -a ~/.zshrc

