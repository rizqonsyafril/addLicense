# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: MilestoneMap
import argparse

def main():
    parser = argparse.ArgumentParser(description='MilestoneMap CLI')
    parser.add_argument('--add', nargs='+', help='Add milestones: name,due,owner,dep1,dep2,...')
    parser.add_argument('--remove', help='Remove milestone by name')
    parser.add_argument('--update', nargs='+', help='Update milestone: name,new_date,new_owner,...')
    parser.add_argument('--report', action='store_true', help='Print milestone report')
    parser.add_argument('--export', help='Export milestones to JSON file')
    args = parser.parse_args()

    if args.add:
        name, due, owner = args.add[0], args.add[1], args.add[2]
        deps = args.add[3:] if len(args.add) > 3 else []
        milestones[name] = {'due': due, 'owner': owner, 'deps': deps}
    elif args.remove:
        if args.remove in milestones:
            del milestones[args.remove]
    elif args.update:
        name = args.update[0]
        if name in milestones:
            for attr in args.update[1:]:
                milestones[name][attr] = args.update[len(args.update)-1]
    elif args.report:
        print('\n'.join(f'{name}: {data}' for name, data in milestones.items()))
    elif args.export:
        import json
        with open(args.export, 'w') as f:
            json.dump(milestones, f, indent=2)
