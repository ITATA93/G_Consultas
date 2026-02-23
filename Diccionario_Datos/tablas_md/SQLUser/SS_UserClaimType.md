# SQLUser.SS_UserClaimType

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLTYPE_ParRef | bigint | PK |  | NO | SS_User Parent Reference |
| CLTYPE_Childsub | double |  |  | NO | Childsub |
| CLTYPE_ClaimType | varchar |  |  | SI | Claim Type |
| CLTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CLTYPE_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*