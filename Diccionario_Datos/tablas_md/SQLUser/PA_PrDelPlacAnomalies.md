# SQLUser.PA_PrDelPlacAnomalies

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PDPA_ParRef | varchar | PK |  | NO | PA_PregDelPlacenta Parent Reference |
| PDPA_Childsub | double |  |  | NO | Childsub |
| PDPA_PlacAnomaly_DR | bigint |  | FK | SI | Des Ref PAC_PlacentaAnomalies |
| PDPA_RowId | varchar |  |  | NO | - |
| PDPA_SortOrder | double |  |  | SI | Sort Order |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*