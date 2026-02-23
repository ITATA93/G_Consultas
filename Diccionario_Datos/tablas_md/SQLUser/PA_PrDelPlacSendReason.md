# SQLUser.PA_PrDelPlacSendReason

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PDSR_ParRef | varchar | PK |  | NO | PA_PregDelPlacenta Parent Reference |
| PDSR_Childsub | double |  |  | NO | Childsub |
| PDSR_RowId | varchar |  |  | NO | - |
| PDSR_SendReason_DR | bigint |  | FK | SI | Des Ref PACPlacentaSendReason |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*