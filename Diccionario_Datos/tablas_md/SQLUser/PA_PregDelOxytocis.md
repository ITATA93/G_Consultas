# SQLUser.PA_PregDelOxytocis

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OXY_ParRef | varchar | PK |  | NO | PA_PregDelivery Parent Reference |
| OXY_Childsub | double |  |  | NO | Childsub |
| OXY_RowId | varchar |  |  | NO | - |
| OXY_ThirdStageOxy_DR | bigint |  | FK | SI | Des Ref ThirdStageOxy |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*