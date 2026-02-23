# SQLUser.IKCSemanticType

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ATUI | varchar |  |  | SI | Unique identifier for attribute |
| CUI | varchar |  |  | SI | Concept Unique Identifier |
| CVF | varchar |  |  | SI | CVF - Content view flag |
| STN | varchar |  |  | SI | Semantic Type Tree Number |
| STY | varchar |  |  | SI | Semantic Type |
| TUI | varchar |  |  | SI | Unique identifier of Semantic type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*