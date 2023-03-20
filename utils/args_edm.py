import argparse


class Args_EDM(argparse.ArgumentParser):
    def __init__(
        self,
    ):
        super().__init__(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        # data param
        self.add_argument("--dataset", default="cata", type=str)
        self.add_argument("--rings_graph", type=bool, default=True)
        self.add_argument("--max-nodes", default=11, type=str)

        # training param
        self.add_argument("--name", type=str, default="cata-test")
        self.add_argument("--restore", type=bool, default=None)
        self.add_argument("--lr", type=float, default=1e-3, help="Learning rate")
        self.add_argument("--num_epochs", type=int, default=1000)
        self.add_argument("--normalize", type=bool, default=True)
        self.add_argument("--num-workers", type=int, default=32)
        self.add_argument("--batch-size", type=int, default=256)
        self.add_argument("--sample-rate", type=float, default=1)

        # Model parameters
        self.add_argument("--dp", type=eval, default=True, help="Data parallelism")
        self.add_argument("--clip_grad", type=eval, default=True, help="True | False")
        self.add_argument("--n_layers", type=int, default=9, help="number of layers")
        self.add_argument("--nf", type=int, default=192, help="number of layers")
        self.add_argument("--tanh", type=eval, default=True)
        self.add_argument("--attention", type=eval, default=True)
        self.add_argument("--coords_range", type=float, default=4)
        self.add_argument("--norm_constant", type=float, default=1)
        self.add_argument("--sin_embedding", type=eval, default=False)
        # EDM
        self.add_argument("--inv_sublayers", type=int, default=1)
        self.add_argument("--normalization_factor", type=float, default=1)
        self.add_argument("--aggregation_method", type=str, default="sum")
        self.add_argument("--diffusion_steps", type=int, default=1000)
        self.add_argument(
            "--diffusion_noise_schedule", type=str, default="polynomial_2"
        )
        self.add_argument(
            "--diffusion_noise_precision",
            type=float,
            default=1e-5,
        )
        self.add_argument("--diffusion_loss_type", type=str, default="l2")
        self.add_argument("--normalize_factors", type=eval, default=[3, 4, 10])

        # Logging
        self.add_argument("--save_dir", type=str, default="summary/")
