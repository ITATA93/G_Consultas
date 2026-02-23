# SQLUser.PA_PrDelLacerations

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PDLACER_ParRef | varchar | PK |  | NO | PA_PregDelivery Parent Reference |
| PDLACER_Childsub | double |  |  | NO | Childsub |
| PDLACER_Loc_DR | bigint |  | FK | SI | Des Ref PAC_LacerationLoc |
| PDLACER_RowId | varchar |  |  | NO | - |
| PDLACER_SortOrder | double |  |  | SI | Sort order |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*