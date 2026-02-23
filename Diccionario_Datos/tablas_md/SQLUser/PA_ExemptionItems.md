# SQLUser.PA_ExemptionItems

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | varchar | PK |  | NO | PA_Exemption Parent Reference |
| ChildQ09DR | - |  |  | SI | Child Reference: Intervención con Prescriptor |
| ITM_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ITM_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_RowId | varchar |  |  | NO | - |
| Q24Q1 | - |  |  | SI | ¿Acepta? |
| Q24Q2 | - |  |  | SI | Motivo Rechazo |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*