# SQLUser.PA_PrDelBabyDelMthd

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PDBDM_ParRef | varchar | PK |  | NO | PA_PregDelBaby Parent Reference |
| PDBDM_Childsub | double |  |  | NO | Childsub |
| PDBDM_DelMthd_DR | bigint |  | FK | SI | Delivery Method DR PAC_DeliveryMethod |
| PDBDM_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*