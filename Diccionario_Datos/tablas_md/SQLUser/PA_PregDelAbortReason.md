# SQLUser.PA_PregDelAbortReason

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ABOR_ParRef | varchar | PK |  | NO | PA_PregDelivery Parent Reference |
| ABOR_Childsub | double |  |  | NO | Childsub |
| ABOR_ReasonAbortion_DR | bigint |  | FK | SI | Des Ref ReasonAbortion |
| ABOR_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*