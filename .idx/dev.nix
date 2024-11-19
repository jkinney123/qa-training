# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
  packages = let
    geckodriverVersion = "0.35.0";
    geckodriver = pkgs.geckodriver.overrideAttrs (oldAttrs: {
      version = geckodriverVersion;
      src = pkgs.fetchurl {
        url = "https://github.com/mozilla/geckodriver/releases/download/v${geckodriverVersion}/geckodriver-v${geckodriverVersion}-linux64.tar.gz";
        sha256 = "0cavjh1pxxgd44q0mshjhh19gcdkmiyknr9zybifj0zn0w6m1dxp";
      };
    });
  in [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.firefox
    geckodriver
  ];


  # Sets environment variables in the workspace
  env = {};
  idx = {
    extensions = [
      # "vscodevim.vim"
    ];

    # Enable previews
    previews = {
      enable = true;
      previews = {
        # web = {
        #   # Example: run "npm run dev" with PORT set to IDX's defined port for previews,
        #   # and show it in IDX's web preview panel
        #   command = ["npm" "run" "dev"];
        #   manager = "web";
        #   env = {
        #     # Environment variables to set for your server
        #     PORT = "$PORT";
        #   };
        # };
      };
    };
    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
        create-venv = ''
          python -m venv .venv
          source .venv/bin/activate
          pip install -r requirements.txt
        '';
      };
      # Runs when the workspace is (re)started
      onStart = {
        # Optionally, activate the virtual environment on start
        activate-venv = "source .venv/bin/activate";
      };
    };
  };
}
