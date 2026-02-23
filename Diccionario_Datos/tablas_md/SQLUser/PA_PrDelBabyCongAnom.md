# SQLUser.PA_PrDelBabyCongAnom

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CA_ParRef | varchar | PK |  | NO | PA_PregDelBaby Parent Reference |
| CA_Childsub | double |  |  | NO | Childsub |
| CA_CongAnom_DR | bigint |  | FK | SI | Des Ref PAC_CongenitalAnomalies |
| CA_RowId | varchar |  |  | NO | - |
| CA_SortOrder | double |  |  | SI | Sort Order |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*