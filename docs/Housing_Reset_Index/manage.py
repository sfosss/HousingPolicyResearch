#!/usr/bin/env python3
import click
import json
import time
import datetime
from pathlib import Path


def log_path(project_root: Path):
    logs = project_root / "00-admin" / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    return logs / (datetime.date.today().isoformat() + ".log")


def write_log(project_root: Path, msg: str):
    lp = log_path(project_root)
    with lp.open("a") as f:
        f.write(f"[{time.strftime('%H:%M:%S')}] {msg}\n")


def ensure_scaffold(project_root: Path):
    for p in [
        "00-admin/index",
        "00-admin/logs",
        "01-sources",
        "02-working",
        "03-outputs",
        "99-archive",
        "templates/prompts",
        "templates/docs",
        "scripts",
    ]:
        (project_root / p).mkdir(parents=True, exist_ok=True)


@click.group()
@click.option("--project-root", required=True, type=click.Path(path_type=Path))
@click.pass_context
def cli(ctx, project_root):
    pr = Path(project_root).expanduser().resolve()
    ctx.obj = {"project_root": pr}
    pr.mkdir(parents=True, exist_ok=True)


@cli.command()
@click.option("--apply", is_flag=True)
@click.pass_context
def reset(ctx, apply):
    pr = ctx.obj["project_root"]
    ensure_scaffold(pr)
    (pr / "00-admin" / "version.json").write_text(
        json.dumps(
            {"version": "0.1", "updated": datetime.date.today().isoformat()}, indent=2
        )
    )
    (pr / "CHANGELOG.md").write_text("# CHANGELOG\n\n- v0.1 Initial scaffold\n")
    click.echo("Reset complete (non-destructive).")


@cli.command()
@click.option(
    "--capstone", "caps", multiple=True, type=click.Path(path_type=Path), required=True
)
@click.option("--types", "types_", default="pdf,docx,md,txt,xlsx,csv")
@click.pass_context
def index(ctx, caps, types_):
    pr = ctx.obj["project_root"]
    ensure_scaffold(pr)
    idx_dir = pr / "00-admin" / "index"
    idx_dir.mkdir(parents=True, exist_ok=True)
    (idx_dir / "sources.jsonl").write_text("[]\n")
    click.echo("Index initialized.")


@cli.command()
@click.option("--template", type=click.Path(path_type=Path), required=True)
@click.pass_context
def master(ctx, template):
    pr = ctx.obj["project_root"]
    ensure_scaffold(pr)
    filename = f"Housing_Subsidy_Reform_MASTER_v0.1_{datetime.date.today().strftime('%Y%m%d')}.docx"
    out = pr / "03-outputs" / filename
    # Create a minimal docx
    from docx import Document

    doc = Document()
    doc.add_heading("NYC Housing Subsidy Reform – Master Policy", 0)
    doc.save(str(out))
    click.echo(f"Master doc written: {out}")


@cli.command()
@click.pass_context
def doctor(ctx):
    pr = ctx.obj["project_root"]
    click.echo("Doctor checks placeholder.")


if __name__ == "__main__":
    cli()
