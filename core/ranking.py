from models.persona import Persona
#from models.geodata import GeoData

class Ranking:
    def rank (data, persona):
        options = {}
        for key in data:
            criterion = data[key]
            value_range = get_range(key, criterion)
            rank_boundaries = get_boundaries(value_range[0], value_range[1])
            options[key] = {}
            options.key["range"] = value_range
            options.key["rangeBoundaries"] = rank_boundaries
        final_ranks = final_rankings(data, options)
        return finalRanks

    def get_range (criterion, values):
        min_value = None
        max_value = None
        persona_range = persona.criteria[criterion].range
        if persona_range:
            min_value = persona_range[0]
            max_value = persona_range[1]
        else:
            min_value = min(values)
            max_value = max(values)
        return [min_value, max_value]

    def get_boundaries (min_value, max_value):
        ranks = []
        for i in xrange(0,6):
            ranks[i] = min_value + (max_value - min_value) * (2**i/64)
        return ranks

    def get_rank (criterion, value, data, options):
        min_value = options[criterion].range[0]
        max_value = options[criterion].range[1]
        if value < min_value or value > max_value:
            for key in data:
                del data[key]
            return -1

        if value == min_value:
            return 0

        current_rank = log(value - min_value/(max_value - min_value)*64,2)
        if persona.criteria[criterion].inverse:
            current_rank = len(options[criterion].rankBoundaries) - current_rank

        # Avoid rank 0 due to 0 * n = 0
        return current_rank

    def total_importance (data, persona):
        # Find total importance/weight
        total_importance = 0
        for criterion in data:
            total_importance += math.sqrt(2) ** (persona.criteria[criterion].importance)
        return total_importance

    def normalise_weights (data):
        # Normalise weights
        criteria = []
        for criterion in data:
            criteria[criterion] = {}
            criteria[criterion].weight = persona.criteria[criterion].importance or 5
            criteria[criterion].normalised_weight = (math.sqrt(2) ** persona.criteria[criterion].importance) / total_importance(data)
        return criteria

    def final_rankings (data, options):
        # Final ranking using weights
        # For each alternative
        final_ranks = {}
        weights = normalise_weights(data)
        for criterion in data:
            final_rank = 0
            for value in data[criterion]:
                rank = get_rank(criterion, value, data, options)
                options[criterion].criterion_rank = rank
                if rank >= 0 and final_rank is not None:
                    options[criterion].normalised_weight = weights[criterion].normalised_weight
                    final_rank += weights[criterion].normalised_weight * options[criterion].criterion_rank
                else:
                    final_rank = None
            if final_rank is not None:
                final_ranks[criterion] = math.round(final_rank);
