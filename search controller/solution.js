@RestController
@RequestMapping("/search")
public class SearchController {

    @Autowired
    private ProductItemRepository productItemRepository;

    @GetMapping
    public ResponseEntity<List<ProductItem>> search(@RequestParam(name = "query", required = false) String query) {
        if (query == null || query.trim().isEmpty()) {
            return ResponseEntity.badRequest().body(Collections.emptyList());
        }
        
        List<ProductItem> products = productItemRepository.findByNameContainingIgnoreCase(query);
        return ResponseEntity.ok(products);
    }
}
