# SQLUser.PA_PrDelPuerpCompl

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PDPC_ParRef | varchar | PK |  | NO | PA_PregDelivery Parent Reference |
| PDPC_Childsub | double |  |  | NO | Childsub |
| PDPC_Complication_DR | bigint |  | FK | SI | Des Ref PAC_Puerperium |
| PDPC_RowId | varchar |  |  | NO | - |
| PDPC_SortOrder | double |  |  | SI | Sort Order |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*