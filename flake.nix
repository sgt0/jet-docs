{
  description = "jet-docs devenv";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem
    (system: let
      pkgs = import nixpkgs {inherit system;};
    in
    {
      devShells = {
        default = pkgs.mkShell
          {
            nativeBuildInputs = with pkgs; [
              alejandra
              nil
              nixd

              python312Packages.pyqt6
              python312Packages.vapoursynth
              uv
              vapoursynth
            ];
          };
      };

      formatter = pkgs.alejandra;
    });
}
